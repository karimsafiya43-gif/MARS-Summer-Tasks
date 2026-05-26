from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='turtlesim',
             executable='turtlesim_node',
             name='sim'),
        Node(package='my_package',
             executable='publisher',
             name='safety_publisher',
             parameters=[{'safety_threshold': 1.5}])])
