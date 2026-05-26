
import rclpy
from rclpy.node import Node
from tutorial_interfaces.srv import SetThresh

class ThresholdClient(Node):
    def __init__(self):
        super().__init__("threshold_client")
        self.client = self.create_client(SetThresh, "threshold")
        self.get_logger().info("Waiting for 'threshold' service...")
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Service not available, retrying...")
        self.get_logger().info("Service found!")
        self.future = None

    def send_request(self):
        new = float(input("Enter new safety threshold value: "))
        if new <= 0:
            self.get_logger().warning("Threshold must be a positive number.")
            return False
        request = SetThresh.Request()
        request.safety_threshold = new
        self.get_logger().info(f"Sending threshold request: {new}")
        self.future = self.client.call_async(request)
        return True


def main():
    rclpy.init()
    node = ThresholdClient()
    if not node.send_request(): 
        node.get_logger().error("Failed to send request. Shutting down.")
        node.destroy_node()
        rclpy.shutdown()
        return
    rclpy.spin_until_future_complete(node,node.future)
    response = node.future.result()
    if response.success is True:
        node.get_logger().info("Threshold updated successfully!")
    else:
       node.get_logger().warning("No threshold update.")
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
