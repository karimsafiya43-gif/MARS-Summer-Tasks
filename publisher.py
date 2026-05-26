# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import Twist
# from rclpy.qos import qos_profile_sensor_data
# from turtlesim.msg import Pose
# from tutorial_interfaces.srv import SetThresh

# class pub(Node):
#     def __init__(self):
#         super().__init__("safety_publisher")
#         self._publishers=self.create_publisher(Twist,'/turtle1/cmd_vel',10)
#         self.subscription=self.create_subscription(Pose,"/turtle1/pose",self.pos_callback,qos_profile_sensor_data)
#         self.declare_parameter("safety_threshold", 1.5)
#         self.safety_threshold=self.get_parameter("safety_threshold").value
#         self.create_timer(1.0,self.v_callback)
#         self.p=None

#         self.service = self.create_service(SetThresh,"threshold",self.threshold_callback )
    
#     def pos_callback(self,msg):
#         self.p=msg   
#     def v_callback(self):
#         vel=Twist()
        
#         if self.p==None:
#             return
#         elif(self.p.x<self.safety_threshold or self.p.x>11-self.safety_threshold or self.p.y<self.safety_threshold or self.p.y>11-self.safety_threshold):
#             self.get_logger().warning(f"alert! turtle is going to hit the wall. ")
#             vel.angular.z=2.0
#             vel.linear.x=0.0
#         else:
#             vel.linear.x=2.0
#             vel.angular.z=0.0
#         self._publishers.publish(vel)

#     def threshold_callback(self,request,response):
#         self.safety_threshold = request.safety_threshold
#         self.set_parameters([rclpy.parameter.Parameter("safety_threshold",rclpy.Parameter.Type.DOUBLE,self.safety_threshold)])
#         self.get_logger().info(f"new threshold value is {self.safety_threshold}")
#         response.success=True
#         return response
       
# def main():
#     rclpy.init()
#     publ=pub()
#     rclpy.spin(publ)
#     publ.destroy_node()
#     rclpy.shutdown()
# if __name__=='__main__':
#     main()

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.qos import qos_profile_sensor_data
from turtlesim.msg import Pose
from tutorial_interfaces.srv import SetThresh


class SafetyPublisher(Node):
    def __init__(self):
        super().__init__("safety_publisher")
        self._publisher = self.create_publisher(Twist,'/turtle1/cmd_vel',10)
        self.subscription = self.create_subscription(Pose,"/turtle1/pose",self.pos_callback,qos_profile_sensor_data)
        self.declare_parameter("safety_threshold", 1.5)
        self.safety_threshold = self.get_parameter("safety_threshold").value
        self.create_timer(1.0,self.v_callback)
        self.p = None
        self.service = self.create_service(SetThresh,"threshold",self.threshold_callback)
        self.get_logger().info("Safety Publisher Node started.")

    def pos_callback(self, msg: Pose):
        self.p = msg

    def v_callback(self):
        if self.p is None:
            return

        vel=Twist()
        x=self.p.x
        y=self.p.y
        thresh=self.safety_threshold

        near_wall=(x<thresh or x>(11-thresh) or y<thresh or y>(11-thresh))

        if near_wall is True:
            self.get_logger().warning(
                f"Turtle near wall — position:({x:.2f}, {y:.2f}), threshold:{thresh}")
            vel.linear.x = 0.0
            vel.angular.z = 2.0
        else:
            vel.linear.x = 2.0
            vel.angular.z = 0.0
        self._publisher.publish(vel)

    def threshold_callback(self,request:SetThresh.Request,response:SetThresh.Response):
        new_thresh = request.safety_threshold
        if new_thresh<=0:
            self.get_logger().warning("Threshold must be positive.")
            response.success=False
            return response
        self.safety_threshold=new_thresh
        self.set_parameters([rclpy.parameter.Parameter("safety_threshold",rclpy.Parameter.Type.DOUBLE,self.safety_threshold)])
        self.get_logger().info(f"Threshold updated to:{self.safety_threshold}")
        response.success = True
        return response


def main():
    rclpy.init()
    node = SafetyPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()