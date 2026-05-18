import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher=self.create_publisher(String,'chatter',20)
        self.timer=self.create_timer(1,self.publish_message)
        self.count=0

    def publish_message(self):
        msg=String()
        msg.data="Hi this is Safiya:"+str(self.count) + " seconds" 
        self.publisher.publish(msg)
        self.get_logger().info('Sent:'+msg.data)
        self.count+=1

def main():
    rclpy.init()
    node=Talker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
