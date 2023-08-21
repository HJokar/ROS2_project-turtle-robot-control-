#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from robot_interfaces.msg import Turtle
from robot_interfaces.msg import TurtleArray
import math as math

class turtle_controllerNode(Node): 
    def __init__(self):
        super().__init__("controller_node")

        #self.targetx=4.0
        #self.targety=8.0
        #self.targettheta=0.0
        self.turtle_to_catch=None

        self.spawn_subscriber_=self.create_subscription(TurtleArray,'alive_turtles',self.callback_alive_turtles,10)
    


        self.Pose_=None


        self.subscriber_=self.create_subscription(Pose,'turtle1/pose',self.callback_turtle1_pose,10)
        self.publisher_=self.create_publisher(Twist,'turtle1/cmd_vel',10)
        self.control_timer_=self.create_timer(0.01,self.Controller)


        self.get_logger().info("the controller node has been started...")

    def callback_alive_turtles(self,msg):
        if len(msg.turtles)>0:
            self.alive_turtles=msg.turtles
            self.turtle_to_catch=self.alive_turtles[0] 

    def callback_turtle1_pose(self,msg):
        #self.get_logger().info('x='+str(msg.x))
        self.Pose_=msg
    


    def Controller(self):
        if self.Pose_==None:
            return
        
        msg=Twist()
        errx=self.turtle_to_catch.x-self.Pose_.x
        erry=self.turtle_to_catch.y-self.Pose_.y
        distance=math.sqrt(errx**2+erry**2)
        goal_ang=math.atan2(erry,errx)
        errtheta=goal_ang-self.Pose_.theta
        if distance>0.5:

            msg.linear.x=distance*2
    
            msg.angular.z=errtheta*6
        else:
            msg.linear.x=0
    
            msg.angular.z=0



        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = turtle_controllerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
