#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
from turtlesim.srv import Kill

from functools import partial
from robot_interfaces.msg import Turtle
from robot_interfaces.msg import TurtleArray
from robot_interfaces.srv import CatchTurtle
import math
import random


class turtleSpawnerNode(Node): 
    def __init__(self):
        super().__init__("turtle_Spawner")
        self.alive_turtles_=[]
        self.get_logger().info('the spawner node has been started')
        self.turtles_publisher_=self.create_publisher(TurtleArray,'alive_turtles',10)
        #self.turtle_publisher_=self.create_publisher(Turtle,'turtle',10)
        self.server_=self.create_service(CatchTurtle,'catch_turtle', self.callback_catch_turtle)
        self.turtle_count_=0
        self.create_timer(2.0,self.new_turtle)


    def callback_catch_turtle(self,request, response):
        nametoremove=request.name
        self.call_Kill_server(nametoremove)
        response.sucess=True
        return response
        


    def publish_alive_turtles(self):
        msg=TurtleArray()
        msg.turtles=self.alive_turtles_
        self.turtles_publisher_.publish(msg)


    def new_turtle(self):
        x=random.uniform(0.0,11.0)
        y=random.uniform(0.0,11.0)
        theta=random.uniform(0.0,2.0)
        name='my_turtle_'+str(self.turtle_count_)
        self.call_spawner_server(x,y,theta,name)
        self.turtle_count_+=1
        new_tur_=Turtle()
        new_tur_.x=x
        new_tur_.y=y
        new_tur_.theta=theta
        new_tur_.name=name
        self.alive_turtles_.append(new_tur_)
        self.publish_alive_turtles()

    def call_Kill_server(self,name):
        client_=self.create_client(Kill,'kill')

        while not client_.wait_for_service(1.0):
            self.get_logger().warn("waiting for the service ...")
        
        request=Kill.Request()
        
  
        request.name=name

        future =client_.call_async(request)
        future.add_done_callback(partial(self.callback_call_kill,name=name))

    def callback_call_kill(self, future,name):
        try:
            future.result()
            for i in range(len(self.alive_turtles_)):
                if self.alive_turtles_[i].name==name:
                    del self.alive_turtles_[i]
                    self.publish_alive_turtles()
                    break


        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))


    def call_spawner_server(self,x,y,theta,name):
        client_=self.create_client(Spawn,'spawn')

        while not client_.wait_for_service(1.0):
            self.get_logger().warn("waiting for the service ...")
        
        request=Spawn.Request()
        
        request.x=x
        request.y=y
        request.theta=theta
        request.name=name

        future =client_.call_async(request)
        future.add_done_callback(partial(self.callback_call_spawn,x=x,y=y,theta=theta,name=name))

    def callback_call_spawn(self, future, x, y,theta,name):
        try:
            response = future.result()
            if response.name is not "":
                self.get_logger().info(f'a new turtle name {name} has been aded at x={x},y={y},theta{theta}')
        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))


def main(args=None):
    rclpy.init(args=args)
    node = turtleSpawnerNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
