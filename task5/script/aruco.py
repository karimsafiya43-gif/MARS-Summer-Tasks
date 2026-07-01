#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

import cv2
import cv2.aruco as aruco
import numpy as np

from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge

from tf2_ros import Buffer, TransformListener
from geometry_msgs.msg import PoseStamped
from tf2_geometry_msgs import do_transform_pose_stamped
from scipy.spatial.transform import Rotation

class ArucoDetector(Node):

    def __init__(self):
        super().__init__('aruco_detector')

        self.bridge = CvBridge()

        self.camera_matrix = None
        self.dist_coeffs = None
        self.marker_size = 0.4
        
        self.tf_buffer=Buffer()
        self.tf_listener=TransformListener(self.tf_buffer,self)
        
        self.image_sub = self.create_subscription(Image,'/camera/image_raw',self.image_callback,10)

        self.info_sub = self.create_subscription(CameraInfo,'/camera/camera_info',self.info_callback,10)

       
        self.aruco_dict = aruco.Dictionary_get(aruco.DICT_7X7_250)
        self.detector_params = aruco.DetectorParameters_create()
        
        self.get_logger().info("ArUco Detector Started — waiting for camera...")
    
    def detector(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        
        corners, ids, rejected = aruco.detectMarkers(gray, self.aruco_dict, parameters=self.detector_params)

        if ids is not None:
            

            
            rvecs, tvecs, _ = aruco.estimatePoseSingleMarkers(corners,self.marker_size,self.camera_matrix,self.dist_coeffs)

            for i in range(len(ids)):
                x = int(corners[i][0][0][0])
                y = int(corners[i][0][0][1])
                text = str(ids[i][0])

                cv2.putText(frame,text,(x + 10, y + 10),cv2.FONT_HERSHEY_COMPLEX_SMALL,1.0,(0, 0, 255),2)

               
                aruco.drawAxis(frame,self.camera_matrix,self.dist_coeffs,rvecs[i],tvecs[i],0.2)

                aruco.drawDetectedMarkers(frame,corners,ids)
                R, _ = cv2.Rodrigues(rvecs[i])
                rot = Rotation.from_matrix(R)
                q = rot.as_quat()  
                roll, pitch, yaw = rot.as_euler('xyz', degrees=False)

                marker = PoseStamped()
                marker.header.frame_id = 'camera_link'
                marker.header.stamp = self.get_clock().now().to_msg()

                marker.pose.position.x = float(tvecs[i][0][2])
                marker.pose.position.y = -float(tvecs[i][0][0])
                marker.pose.position.z = -float(tvecs[i][0][1])
                marker.pose.orientation.x = q[0]
                marker.pose.orientation.y = q[1]
                marker.pose.orientation.z = q[2]
                marker.pose.orientation.w = q[3]
             

                try:
                    transform = self.tf_buffer.lookup_transform('odom', 'camera_link',rclpy.time.Time())

                    marker_world = do_transform_pose_stamped(marker, transform)

                    self.get_logger().info(f"ID {ids[i][0]} "
                                           f"x={marker_world.pose.position.x:.3f} "
                                           f"y={marker_world.pose.position.y:.3f} "
                                           f"z={marker_world.pose.position.z:.3f} "
                                           f"quaternion=({marker_world.pose.orientation.x:.3f}, "
                                           f"{marker_world.pose.orientation.y:.3f}, "
                                           f"{marker_world.pose.orientation.z:.3f}, "
                                           f"{marker_world.pose.orientation.w:.3f})"
                                           f"RPY (rad): roll={roll:.3f}, pitch={pitch:.3f}, yaw={yaw:.3f}")
                    
                    
                except Exception as e:
                    self.get_logger().warn(f'TF error: {e}')
                

        else:
            self.get_logger().info("Waiting for marker...", throttle_duration_sec=2.0)

        cv2.imshow("ArUco Detection", frame)
        cv2.waitKey(1)

    def info_callback(self, msg):
        self.camera_matrix = np.array(msg.k).reshape(3, 3)
        self.dist_coeffs = np.array(msg.d)

    def image_callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
       
        if self.camera_matrix is None:
            return

        if not hasattr(self, 'recorder'):
            h, w = frame.shape[:2]
            codec = cv2.VideoWriter_fourcc(*'XVID')
            self.recorder = cv2.VideoWriter(
                'myvideo.avi',
                codec,
                20,
                (w, h)
            )

        self.detector(frame)
        self.recorder.write(frame)


def main(args=None):
    rclpy.init(args=args)
    node = ArucoDetector()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Node interrupted.")
    finally:
        if hasattr(node, 'recorder'):
            node.recorder.release()
        node.destroy_node()
        cv2.destroyAllWindows()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
