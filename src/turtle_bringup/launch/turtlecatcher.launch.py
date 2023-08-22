from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld=LaunchDescription()

    turtlesim_node_=Node(
        package='turtlesim',
        executable='turtlesim_node'
    )

    turtle_spawner_node_=Node(
        package="turtle_project",
        executable="turtle_spawner_node",
        parameters=[{'spawn_period': 0.5}]
    )

    turtle_controller_node_=Node(
        package="turtle_project",
        executable="turtle_controller",
        parameters=[{'frequency_controller': 50.0}])

    ld.add_action(turtlesim_node_)
    ld.add_action(turtle_spawner_node_)
    ld.add_action(turtle_controller_node_)






    return ld