#SAFIYA CS25B1003
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.subscriptionnn=self.create_subscription(String,'chatter',self.listener_callback,20)
    def listener_callback(self,msg):
        self.get_logger().info("I heard "+msg.data+" from talker") 

def main():
    rclpy.init()
    node=Listener()
    rclpy.spin(node)
    node.destroy_node
    rclpy.shutdown()
if __name__ == '__main__':
    main()


