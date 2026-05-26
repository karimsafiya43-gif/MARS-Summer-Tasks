import time
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from rclpy.action import ActionServer
from rclpy.qos import qos_profile_sensor_data
from action_tutorials_interfaces.action import ExecuteCircle
from math import sqrt

class CircleServer(Node):
    def __init__(self):
        super().__init__('circle_patrol_server')
        self.vel = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pos = self.create_subscription(Pose, '/turtle1/pose', self.pos_callback, qos_profile_sensor_data)
        self.action = ActionServer(self, ExecuteCircle, 'execute_circle', self.execute_callback)
        self.pose = None
        self.safety_threshold = 1.5

    def pos_callback(self, msg):
        self.pose = msg

    def execute_callback(self, goal_handle):
        while self.pose is None:
            self.get_logger().info("Waiting for position data...")
            rclpy.spin_once(self, timeout_sec=0.5)
        start_x = self.pose.x
        start_y = self.pose.y
        v = 1.5
        r = goal_handle.request.radius
        w = v / r
        tolerance = 0.2
        fback_msg = ExecuteCircle.Feedback()
        result = ExecuteCircle.Result()
        velo = Twist()
        total_arclength = 0.0
        prev_x = start_x
        prev_y = start_y
        moved = False
        thresh = self.safety_threshold
        self.get_logger().info(f"Starting moving in radius:{r}, v:{v}, w:{w:.2f}")
        while True:
            rclpy.spin_once(self, timeout_sec=0.05)
            x = self.pose.x
            y = self.pose.y
            near_wall = (x < thresh or x > (11-thresh) or y < thresh or y > (11-thresh))
            if near_wall:
                velo.linear.x = 0.0
                velo.angular.z = 0.0
                self.vel.publish(velo)
                fback_msg.success = False
                fback_msg.final_report = "aborted - near wall"
                goal_handle.publish_feedback(fback_msg)
                goal_handle.abort()
                result.distance_travelled = total_arclength
                result.current_status = "aborted"
                self.get_logger().info(f"Mission Aborted: Boundary Collision Imminent!")
                return result
            dx = x - prev_x
            dy = y - prev_y
            total_arclength += sqrt(dx**2 + dy**2)
            prev_x = x
            prev_y = y
            begin_dist = sqrt((x - start_x)**2 + (y - start_y)**2)
            fback_msg.success = True
            fback_msg.final_report = f"moving... arclength: {total_arclength:.2f}"
            goal_handle.publish_feedback(fback_msg)
            if not moved and begin_dist > tolerance:
                moved = True
            else:
                if moved and begin_dist < tolerance:
                    velo.linear.x = 0.0
                    velo.angular.z = 0.0
                    self.vel.publish(velo)
                    goal_handle.succeed()
                    result.distance_travelled = total_arclength
                    result.current_status = "completed"
                    self.get_logger().info(f"full Circle movement Completed! distance covered is {total_arclength:.2f}")
                    return result
            velo.linear.x = v
            velo.angular.z = w
            self.vel.publish(velo)
            time.sleep(0.1)

def main(args=None):
    rclpy.init(args=args)
    circle_server = CircleServer()
    rclpy.spin(circle_server)
    circle_server.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()