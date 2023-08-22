cmake_minimum_required(VERSION 3.8)
project(robot_interfaces)



# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Turtle.msg"
  "msg/TurtleArray.msg"
  "srv/CatchTurtle.srv"
  # other message files if any
)

ament_package()
