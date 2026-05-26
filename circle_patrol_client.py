import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from action_tutorials_interfaces.action import ExecuteCircle

class CircleClient(Node):
    def __init__(self):
        super().__init__('circle_patrol_client')
        self.action_client = ActionClient(self, ExecuteCircle,'execute_circle')

    def goal_to_server(self, radius):
        self.get_logger().info("waiting for action server..")
        self.action_client.wait_for_server()
        goal_msg = ExecuteCircle.Goal()
        goal_msg.radius = radius
        self.get_logger().info(f"Sending goal with radius: {radius}")
        self.future = self.action_client.send_goal_async(goal_msg, feedback_callback=self.get_feedback)
        self.future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self,future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info("Goal Rejected")
            return
        self.get_logger().info("Goal Accepted")
        self.future_result = goal_handle.get_result_async()
        self.future_result.add_done_callback(self.get_result_callback)

    def get_feedback(self,fback_msg):
        fb = fback_msg.feedback
        self.get_logger().info(f"success: {fb.success}, arclength: {fb.final_report}")

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f"distance travelled:{result.distance_travelled}, status:{result.current_status}")


def main(args=None):
    rclpy.init(args=args)
    node = CircleClient()
    radius = float(input("Enter radius: "))
    node.goal_to_server(radius)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
