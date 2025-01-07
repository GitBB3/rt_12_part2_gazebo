#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class RobotMover(Node):
    def __init__(self):
        super().__init__('robot_mover')

        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)

        self.timer = self.create_timer(0.1, self.move_robot)

    def move_robot(self):
        move_cmd = Twist()
        move_cmd.linear.x = 0.5  # Linear speed Vx
        move_cmd.angular.z = 0.1  # Angular speed Wz

        self.publisher_.publish(move_cmd)
        self.get_logger().info(f"Command: Vx={move_cmd.linear.x}, Wz={move_cmd.angular.z}")


def main(args=None):
    rclpy.init(args=args)
    node = RobotMover()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

