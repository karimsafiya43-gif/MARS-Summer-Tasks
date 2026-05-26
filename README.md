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



























   

   




  
  
  
  
   
   
   
   
