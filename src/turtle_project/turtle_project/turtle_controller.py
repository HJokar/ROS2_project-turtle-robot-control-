#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from robot_interfaces.msg import Turtle
from robot_interfaces.msg import TurtleArray
from robot_interfaces.srv import CatchTurtle
from functools import partial


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
        self.declare_parameter("frequency_controller",50.0)
        self.frequency_controller_=self.get_parameter("frequency_controller").value
        self.control_timer_=self.create_timer(1/self.frequency_controller_,self.Controller)


        self.get_logger().info("the controller node has been started...")

    def callback_alive_turtles(self,msg):
        if len(msg.turtles)>0:
            self.alive_turtles=msg.turtles
            #self.turtle_to_catch=self.alive_turtles[0]
            distance =math.inf
            for i in range(len(self.alive_turtles)):
                errx=self.alive_turtles[i].x-self.Pose_.x
                erry=self.alive_turtles[i].y-self.Pose_.y
                distancen=math.sqrt(errx**2+erry**2)
                if distancen<distance:
                    self.turtle_to_catch=self.alive_turtles[i]
                    distance=distancen



    def callback_turtle1_pose(self,msg):
        #self.get_logger().info('x='+str(msg.x))
        self.Pose_=msg
    
    def call_Catch_turtle_server(self,name):
        client_=self.create_client(CatchTurtle,'catch_turtle')

        while not client_.wait_for_service(1.0):
            self.get_logger().warn("waiting for the service ...")
        
        request=CatchTurtle.Request()
        
  
        request.name=name

        future =client_.call_async(request)
        future.add_done_callback(partial(self.callback_call_Catch_turtle,name=name))

    def callback_call_Catch_turtle(self, future,name):
        try:
            response = future.result()
            if not response.sucess:
                self.get_logger().error(f"the turtle with name {name} can not be caught")
            


        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))


    


    def Controller(self):
        if self.Pose_==None or self.turtle_to_catch==None:
            return
        
        msg=Twist()
        errx=self.turtle_to_catch.x-self.Pose_.x
        erry=self.turtle_to_catch.y-self.Pose_.y
        distance=math.sqrt(errx**2+erry**2)
        goal_ang=math.atan2(erry,errx)
        errtheta=goal_ang-self.Pose_.theta

        if errtheta>math.pi:
            errtheta-=2*math.pi
        elif errtheta<-math.pi:
            errtheta+=2*math.pi

        if distance>0.5:

            msg.linear.x=distance*2
    
            msg.angular.z=errtheta*6
        else:
            msg.linear.x=0.0
    
            msg.angular.z=0.0
            self.call_Catch_turtle_server(self.turtle_to_catch.name)
            self.turtle_to_catch=None



        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = turtle_controllerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
