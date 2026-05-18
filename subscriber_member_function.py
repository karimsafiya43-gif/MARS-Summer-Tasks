# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import String



# class Subscriber(Node):
#     def __init__(self):
#         super().__init__('subscriber')
#         self.subscribe=self.create_subscription(String,'topic',self.subscriber_callback,10)
#     def subscriber_callback(self,msg):
#         self.get_logger().info('Data received "%s"' % msg.data)



# def main(args=None):
#     rclpy.init(args=args)
#     minimal_subscriber = Subscriber()
#     rclpy.spin(minimal_subscriber)
#     minimal_subscriber.destroy_node()
#     rclpy.shutdown()


# if __name__ == '__main__':
#     main()

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


