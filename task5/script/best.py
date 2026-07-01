#!/usr/bin/env python3

import cv2
import numpy as np

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge

from ultralytics import YOLO


class YOLODetector(Node):

    def __init__(self):
        super().__init__("yolo_detector")
        self.bridge = CvBridge()
        self.model = YOLO("/home/safiya/ros2_ws/src/rover/script/content/runs/detect/train/weights/best.pt")
        self.camera_matrix = None
        self.dist_coeffs = None
        self.subscription = self.create_subscription(
            Image,
            "/camera/image_raw",
            self.callback,
            10
        )
        self.info_sub = self.create_subscription(
            CameraInfo,
            '/camera/camera_info',
            self.info_callback,
            10
        )
        

        self.get_logger().info("YOLO Detector Started ")
        
    def info_callback(self,msg):       
        self.camera_matrix = np.array(msg.k).reshape(3, 3)

        self.dist_coeffs = np.array(msg.d)

    def callback(self, msg):
        
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        frame = np.ascontiguousarray(frame, dtype=np.uint8)
        results = self.model(frame,verbose=False)
        result = results[0]
        annotated_frame = result.plot()
        cv2.imshow("YOLO Detection",annotated_frame)
        cv2.waitKey(1)


def main(args=None):

    rclpy.init(args=args)
    node = YOLODetector()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    cv2.destroyAllWindows()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
