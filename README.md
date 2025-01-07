# robot_urdf
Assignment 2 part 2 (repository is the version in the turtlesim environment, this is the required version with RViz and Gazebo)

## Run it

ros2 launch robot_urdf gazebo.launch.py

## Change the velocity command
The current command is a linear velocity of Vx = 0.5 and an angular velocity of Wz = 0.1.

## Modifications compared to the original repository

### robot_move.py
Is the executable written in the directory scripts/ to implement the publisher which publishes velocity command to the robot with cmd_vel. It is a modified and easier version of the one made for the turtlesim environment in the "rt_12" repository.

### gazebo.launch.py
Has been modified to launch the node created in robot_move.py.

The node is defined (ls 38-42): 
	robot_move_node = Node(
		package='robot_urdf',
		executable='robot_move.py',
		name='robot_move',
		output='screen')

and then launched (l.56):
	robot_move_node

### CMakeLists.txt
In the CMakeLists.txt, we include the new dependencies used in robot_move.py (ls 23-24):
	find_package(rclpy REQUIRED)
	find_package(geometry_msgs REQUIRED)

and we declare the executable (ls 31-34):
	install(PROGRAMS
	  scripts/robot_move.py
	  DESTINATION lib/${PROJECT_NAME}
	)
