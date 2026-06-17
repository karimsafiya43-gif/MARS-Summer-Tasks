# MARS-Summer-Tasks

USE UBUNTU Jammy 22.04 for running ROS2 Humble 

1. INSTALL ROS2
   
   1.set locale to UTF-8
   
   2.setup sources: add ros2 apt repository to system
   
   3.update your system for latest version
   
   4.install ros-humble
   
   5.Environment setup: by sourcing the file (source /opt/ros/humble/setup.bash)
   
   6. run a demo talker and listener node in two differnt terminal window

2.BASIC SETUP

   1. source the setup file (add it to shell startup script .bashrc)
        source /opt/ros/humble/setup.bash
      
   2. Domain id setup (nodes with same domain id can communicate) and add to shell startup
      
   3. set ROS_LOCALHOST_ONLY to 1 (my nodes,topics, services etc. will be used by me only) and add to shell startup

3. TURTLESIM DEMO
   
   1.install turtlesim

   2.check for the installed packages

   3.run turtlesim turtlesim_node (graphical display)

   4.run teleop node to control the movement of turtle

   5.install rqt and run it to access services

   6. spawn(new turtle) ,set_pen to modify colour rgb and thickness

   7. remap cmd_vel topic and rotate_absolute action to the turtle2

4.graphs and nodes
   
   1.remapping: to change the name of node turtlesim to my_turtle 
    
   2.node info: gives the information about node, its publishers, subscribers, topics etc.
    
5.topics
 
   1.rqt_graph can be used to get a diagrammamtic view of how nodes interact with each other over topics
  
   2.topic list: to view all the topics/communication channels
  
   3.topic list -t: topic list with type
  
   4.topic echo: will print the data communicated over a topic
  
   5.topic info: gives the information about a topic 
  
   6. --verbose: for more detailed info
  
   7. interface show : to get details about msg type
  
   8. ros2 topic pub : to publish a msg to the topi
  
   9.topic hz: to display speed to sending msgs
  
   10.topic bw: bandwidth and number of msgs sent
  
   11. topic find: to find topic with a given msg type

6.services
 
  1.service list: to view list of active services
  
  2.service type: to see the type of a service
  
  3. -t: to see all the active services type
  
  4. service find: to find the service with a given type
  
  5. interface show: to see the structure of a service 
  
  6. service call: used to call a service

7.Parameters

  1.param list: used to view list of active parameters
 
  2.param set: to set value of a given parameter
  
  3.param get: to output the value of a parameter
  
  4. param dump: to view all values of all parameters 
  
  5.param load: to load the parameters from a file to a running node
  
  6.Load parameter file on node startup: node neednot be running at present

8.Actions(for long running tasks):

  client server format
    
   1.actions on the teleop node
    
   2.action list:displays the list of actions
    
   3.-t: type of an action
    
   4.action info: detailed info about an action
    
   5.interface show: structure of action
    
   6.action send_goal: gives the goal value for an action

 
 9. rqt_console :

     view and filter log msgs
       1.  Fatal
       2.  Error
       3.  Warn
       4.  Info
       5.  Debug
   
10. recording and playing data:
      
    1.ros2 bag: command line tool to record data published on a topic
       
    2. record: to record the values of a topic
       
    3. bag info: display information about the recording
       
    4. bag play: to play the contents of a bag

CLIENT LIBRARIES


COLCON: tool used to build workspaces.
       
   It creates ready-to-run ROS 2 programs


1.ros2 WORKSPACE:
   
   1.src/: packages go here
   
   2.build/: temporary files go here
   
   3.install/: final runnable files
   
   4.log/: helps to build logs


steps to build workspace:


1.source ros2 environment- underlay:

  source /opt/ros/humble/setup.bash
  
2. go to workspace and source

     cd ~/ros2_ws/src

4.for sample: clone the ros_tutorial package into your workspace

   git clone https://github.com/ros/ros_tutorials.git -b humble

6. back to ros2_ws and install all dependencies listed

   rosdep install -i --from-path src --rosdistro humble -y

5.build the packages 

colcon build --executor sequential

6.source the underlay followed by overlay

 source /opt/ros/humble/setup.bash
 
 source install/local_setup.bash

2.CREATING PACKAGE:
 
   Package creation in ROS 2 uses ament as its build system and colcon as its build tool.

   Content inside CMake package:
   
      1.CMakeLists.txt
      2.include/<package_name>
      3.package.xml
      4.src

   Inside Python package:
  
      1. package.xml
      2.resource/my_package
      3.setup.cfg
      4.setup.py
      5.my_package/

   1.move to src
      
       cd ros2_ws
       
       cd src

   2.command to create a new package
      
      CPP:
      
         ros2 pkg create --build-type ament_cmake --license Apache-2.0 --node-name my_node my_package
      
      PYTHON:
      
         ros2 pkg create --build-type ament_python --license Apache-2.0 --node-name my_node my_package

   3.Build the package:
         
         return to ros2_ws
         
         colcon build --packages-select my_package//to build a particular package

   4.source the setup file:
         
         source install/local_setup.bash
   
   5.run the package:
         
         ros2 run my_package my_node

   CPP/CMAKE:
   
   6.open package.xml and modify the following:
   
         name and email in mainainer
         
         change the description: here <description>Beginner client libraries tutorials practice package</description>
         
         update license line: <license>Apache License 2.0</license>
        
   PYTHON
   
   6.open setup.py make the exact same changes


3.CREATING A NODE:
   
   consists of a publisher and a subscriber 
   
CPP:

   1.create a package 

      ros2 pkg create --build-type ament_cmake --license Apache-2.0 cpp_pubsub

   2.ros2_ws/src/cpp_pubsub/src write publisher node 

   3.go to package.xml and edit
   
      <description>Examples of minimal publisher/subscriber using rclcpp</description>
      <maintainer email="you@email.com">Your Name</maintainer>
      <license>Apache License 2.0</license>

   after ament_cmake
   
      <depend>rclcpp</depend>
      <depend>std_msgs</depend>

   to use these libraries

   4.Go to CMakeLists.txt file

   below ament_cmake REQUIRED add:
      
      find_package(rclcpp REQUIRED)
      find_package(std_msgs REQUIRED)
      
      add_executable(talker src/publisher_member_function.cpp)
      ament_target_dependencies(talker rclcpp std_msgs)
      
      install(TARGETS
        talker
        DESTINATION lib/${PROJECT_NAME})

   5. write the subscriber node

      1.open CMakeLists.txt and add:

         add_executable(listener src/subscriber_member_function.cpp)
         ament_target_dependencies(listener rclcpp std_msgs)

         install(TARGETS
           talker
           listener
           DESTINATION lib/${PROJECT_NAME})

      
   6. install missing dependencies

           rosdep install -i --from-path src --rosdistro humble -y

   7. build new package

             colcon build --packages-select cpp_pubsub

   8. source setup files:

         . install/setup.bash


PYTHON:

   1.create package

      ros2 pkg create --build-type ament_python --license Apache-2.0 py_pubsub

   2.ros2_ws/src/py_pubsub/py_pubsub write a publisher and a subscriber node

   3. go to package.xml

      edit:

      <description>Examples of minimal publisher/subscriber using rclpy</description>
      <maintainer email="you@email.com">Your Name</maintainer>
      <license>Apache License 2.0</license>

   4.and add:

      <exec_depend>rclpy</exec_depend>
      <exec_depend>std_msgs</exec_depend>
            
   5. go to setup.py

      1. add an entry point:

           check this:
               maintainer='YourName',
               maintainer_email='you@email.com',
               description='Examples of minimal publisher/subscriber using rclpy',
               license='Apache License 2.0',
         

      in console script bracket:

                            'talker = py_pubsub.publisher_member_function:main',
                                  'listener = py_pubsub.subscriber_member_function:main',
         

   6. install dependencies
   
         rosdep install -i --from-path src --rosdistro humble -y

   7.build new package and source the setup 

   colcon build --packages-select py_pubsub
   source install/setup.bash

   8.run the node

   -----------------------------------------------------------------------------------------------------------------------------------------------

   PARAMETERS:

   METHODS:

      declare_parameter()	--- Declare a parameter
      get_parameter() ---	Read parameter value
      set_parameters() --- Change parameter values

   ACTION SERVER

   METHODS:

      ActionServer()	--- Create action server
      execute_callback() ---	Executes goal
      goal_callback() ---	Accept/reject goal
      publish_feedback() ---Send feedback
      succeed() ---	Mark goal success
      abort() ---	Mark goal failed


   ACTION CLIENT

   METHODS:

         ActionClient()	--- Create action client
         wait_for_server()	--- Wait until server available
         send_goal_async()	--- Send goal asynchronously
         get_result_async() --- Get result asynchronously

SERVICE SERVER:

METHODS:

      create_client() ---	Create service client
      wait_for_service() ---	Wait until service available
      call_async() ---	Send async request

SERVICE CLIENT:

METHODS:

      create_client() --- Create service client
      wait_for_service() --- Wait until service available
      call_async() --- Send async request

QOS - quality of service 

Tells about the parameters on which communication between the publisher and subscriber takes place.

These parameters are called policies.

Reliability:
Tells if each msg must be delivered or not.

   Reliable: all msgs must arrive.
   Best Effort: msgs sent without the confirmation if they arrived or not

History:
Tells how many msgs should be stored.

   Keep Last: upto n old msgs are stored
   Keep All: store all msgs

Durability:
Should new users have access to old msgs...

   Volatile:
   Active subscribers receive msgs
   Transient local:
   new subscribers can receive old msgs also.

for sensor data,
qos is of the form:

         Reliability	    Best Effort
         History	       Keep Last
         Queue Depth	    Small
         Durability	    Volatile


LAUNCH FILES:
files that are used to launch multiple nodes by its execution at the same time.

arguments of a node in alaunch file are as follows:

         package	   package name
         executable	node executable
         name	      node name
         output	   terminal output
         parameters	enter parameters
         remappings	change topic names
----------------------------------------------------------------------------------------------------------------------------

Installing GAZEBO ignition:

BINARY INSTALL:

      sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
      wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
      sudo apt-get update
      
      sudo apt-get install libignition-gazebo6-dev

SOURCE INSTALL:

      sudo apt install -y build-essential cmake git gnupg lsb-release wget
      
      sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
      
      wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
      sudo apt-get update
      
      git clone https://github.com/ignitionrobotics/ign-gazebo -b ign-gazebo6
      
      sudo apt -y install \
        $(sort -u $(find . -iname 'packages-'`lsb_release -cs`'.apt' -o -iname 'packages.apt' | tr '\n' ' '))
      
      cd ign-gazebo
      mkdir build
      cd build
      cmake ../
      make



package.xml

This tells ROS 2 what dependencies our package needs to compile and run.

      <exec_depend>rclpy</exec_depend>
        <exec_depend>robot_state_publisher</exec_depend>
        <exec_depend>xacro</exec_depend>
        <exec_depend>ros_gz_sim</exec_depend>
CMakeLists.txt

This file ensures that your urdf, launch, and sdf folders are safely installed and accessible when you compile your workspace with colcon build.
add this:

      install(
        DIRECTORY launch urdf sdf
        DESTINATION share/${PROJECT_NAME}
      )


To define our robot's physical structure, visual appearance, and physics, this package utilizes URDF and Xacro files. 

1. URDF (Unified Robot Description Format)
   An XML file format used in ROS 2 to describe all the physical elements of a robot.

Components:
      
      Links: Represent the physical parts of the robot (chassis, wheels, sensors) and define their shape, mass, visual       color, and collision boundaries.
      Joints: Connect two links together and define how they move relative to each other (e.g., fixed, revolute/            rotating, continuous).

2. Xacro (XML Macros)
   
         An upgrade for URDF that turns a plain, XML file into a smart template. It lets us use shortcuts, math, and
         variables so you don't have to re-type the same code over and over.

Properties (variables) : Allows us to define a value once (like wheel radius or chassis weight) and reuse it everywhere. If a dimension changes, we only update it in one place.
Macros (Functions): Allows us to write a block of code once (like a template for a wheel assembly) and reuse it multiple times with different arguments.

It's easiest to just put this in every robot tag, so that you always have the option of using xacro if you want.

      <robot xmlns:xacro="http://www.ros.org/wiki/xacro">

 To include another file we use the xacro:include tag like this:

      <xacro:include filename="include.xacro" />

3. SDF (Simulation Description Format)
   
 An XML file format used  by Gazebo to describe the *world* outside of the robot. While URDF only describes the robot itself, SDF describes everything else in the environment.
 
   World Building:It defines the environment elements, including the ground plane, lighting (the sun), gravity, and sky          
   properties.
   Obstacles & Environment:* It is used to place 3D objects, walls, barriers,  into the world so the robot has things to interact with or avoid.
   Physics Properties: It controls how objects behave physically—whether they are static (frozen in place like a heavy concrete wall) or dynamic (can fall over or move when pushed).
   

BUILD THE PACKAGE

            cd ~/ros2_ws
            colcon build --packages-select my_robot_simulation
            source install/setup.bash

install the graphical user interface tool that lets you control your robot's non-fixed joints using sliders

      sudo apt install ros-humble-joint-state-publisher-gui

link between ros and gazebo

      sudo apt install ros-humble-ros-ign-gazebo
      sudo apt install ros-humble-ros-ign-bridge

System Plugin = code that controls simulation behavior
A plugin is a piece of code that adds extra functionality to Gazebo without modifying Gazebo itself.

      Physics Settings
      ├── Gravity
      ├── Simulation Speed
      ├── Time Step
      ├── Collision Handling
      └── Solver Settings

Physics

         <plugin
           filename="gz-sim-physics-system"
           name="gz::sim::systems::Physics"/>

Handles:

      Gravity
      Collisions
      Friction
      Joint dynamics

UserCommands

      <plugin
        filename="gz-sim-user-commands-system"
        name="gz::sim::systems::UserCommands"/>

Allows:

      Insert models
      Delete models
      Move models from GUI

SceneBroadcaster

      <plugin
        filename="gz-sim-scene-broadcaster-system"
        name="gz::sim::systems::SceneBroadcaster"/>

<img width="1827" height="1056" alt="Screenshot from 2026-06-17 17-16-56" src="https://github.com/user-attachments/assets/a1bbb5af-6755-4643-b90a-e659d4376604" />
<img width="1827" height="1056" alt="Screenshot from 2026-06-17 17-16-38" src="https://github.com/user-attachments/assets/a17ac66c-3dac-4107-9cff-1a2f523a92db" />
<img width="1827" height="1056" alt="Screenshot from 2026-06-17 17-10-43" src="https://github.com/user-attachments/assets/9f21273f-bf9c-49e5-a74c-75d40e617644" />
<img width="1827" height="1056" alt="Screenshot from 2026-06-17 17-10-03" src="https://github.com/user-attachments/assets/1f431fe3-5f60-4484-ad06-64f2f86db3ac" />
<img width="1827" height="1056" alt="Screenshot from 2026-06-17 17-09-27" src="https://github.com/user-attachments/assets/0e471682-5ecf-4ef2-a997-85123d5da176" />
<img width="1827" height="1007" alt="Screenshot from 2026-06-17 17-08-57" src="https://github.com/user-attachments/assets/c5d65a5a-d206-4646-bf97-631100f9b8d2" />


SENSOR IMPLEMEMTATION:

1.Camera sensor
2.Lidar sensor 
3.IMU sensor


Camera Sensor

A RGB camera is mounted on the robot arm and used for visual perception.

Attached to camera_link (mounted on arm)
Gazebo sensor type: camera
Publishes RGB images to ROS 2

Parameters:

Resolution: 640 × 480
Frame rate: 30 Hz
Field of View: 1.047 rad
Noise: Gaussian noise

ROS Topics:

/camera/image_raw → sensor_msgs/Image
/camera/camera_info → sensor_msgs/CameraInfo

LiDAR Sensor
A 2D GPU-based LiDAR is mounted on a mast for obstacle detection.

Attached to laser_frame
Gazebo sensor type: gpu_lidar
Provides 360° planar scan

Key Parameters:

Samples: 720 rays per scan
Range: 0.1 m to 30 m
Update rate: 10 Hz

ROS Topic:
/scan → sensor_msgs/LaserScan

IMU Sensor
An Inertial Measurement Unit (IMU) is placed at the robot base to estimate motion dynamics.

Attached to imu_link on base_l
Gazebo sensor type: imu
Provides orientation, velocity and acceleration

Key Parameters:

Update rate: 50 Hz
Gaussian noise added to simulate real-world sensor atmosphere

ROS Topic:

/imu → sensor_msgs/Imu

ROS 2 bridging

All sensors are integrated into ROS 2 using ros_gz_bridge, which converts Gazebo messages into ROS 2 topics:


BRIDGES:

      Converts Gazebo sensor outputs → ROS 2 topics
      Converts ROS 2 commands → Gazebo control inputs

      Camera → sensor_msgs/Image
      LiDAR → sensor_msgs/LaserScan
      IMU → sensor_msgs/Imu


      | ROS 2 Topic           | ROS Message Type             | Gazebo Message Type        | Detail                          |
      | `/joint_states`       | `sensor_msgs/msg/JointState` | `ignition.msgs.Model`      | Wheel joint state publishing    |
      | `/camera/image_raw`   | `sensor_msgs/msg/Image`      | `ignition.msgs.Image`      | RGB camera feed                 |
      | `/camera/camera_info` | `sensor_msgs/msg/CameraInfo` | `ignition.msgs.CameraInfo` | Camera calibration data         |
      | `/cmd_vel`            | `geometry_msgs/msg/Twist`    | `ignition.msgs.Twist`      | Robot velocity control          |
      | `/odom`               | `nav_msgs/msg/Odometry`      | `ignition.msgs.Odometry`   | Odometry data from diff-drive   |
      | `/scan`               | `sensor_msgs/msg/LaserScan`  | `ignition.msgs.LaserScan`  | LiDAR scan data                 |
      | `/imu`                | `sensor_msgs/msg/Imu`        | `ignition.msgs.IMU`        | IMU sensor data                 |


The plugins used for establising the gazebo environment and the motion, sensor implementation are:

The robot simulation uses multiple Ignition Gazebo system plugins for physics, sensors, and robot control.

Sensor Plugins

Sensors System Plugin

      ignition::gazebo::systems::Sensors
      
Manages all sensors (camera, LiDAR, IMU)

IMU Sensor Plugin

      ignition::gazebo::systems::Imu
      
Provides orientation,velocity and acceleration with noise

Robot Control Plugins

Diff Drive plugin

      ignition::gazebo::systems::DiffDrive
      
Controls 4-wheel differential drive robot

         Subscribes: /cmd_vel
         Publishes: /odom

ROS 2 Control Plugin

      ign_ros2_control::IgnitionROS2ControlPlugin
      
Loads controller configuration from controllers.yaml

Joint State Publisher Plugin

      ignition::gazebo::systems::JointStatePublisher
      
Publishes wheel joint states to /joint_states

for controlling the wheels and motion of rover install teleop keyboard and run it:

       sudo apt install ros-humble-teleop-twist-keyboard
       ros2 run teleop_twist_keyboard teleop_twist_keyboard

For arm joint controller install:

      sudo apt install ros-humble-rqt ros-humble-rqt-controller-manager ros-humble-rqt-joint-trajectory-controller

to run it 

      rqt

The arm joint (base_to_arm) is controlled using a ROS 2 controller:

   Controller Type: Joint trajectory controller
   Joint: base_to_arm
   Interfaces:
   command: position
   state: position, velocity


      












  


























   

   




  
  
  
  
   
   
   
   
