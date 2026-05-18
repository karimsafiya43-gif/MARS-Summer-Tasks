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
      
   3. Domain id setup (nodes with same domain id can communicate) and add to shell startup
      
   4. set ROS_LOCALHOST_ONLY to 1 (my nodes,topics, services etc. will be used by me only) and add to shell startup

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
   
  11. recording and playing data:
      
       1.ros2 bag: command line tool to record data published on a topic
       
       2. record: to record the values of a topic
       
       3. bag info: display information about the recording
       
       4. bag play: to play the contents of a bag
          

  
  
  
  
   
   
   
   
