Step 1: Create the turtle_controller node, subscribe to /turtle1/pose. Create a control
loop to reach a given target (for now an arbitrary one). A little bit of math will be required
to find the distances and angles. And send the command to the /turtle1/cmd_vel topic.
Step 2: Create the turtle_spawner node. With a timer, spawn a new turtle at a given rate.
To spawn a turtle, call the /spawn service.
Step 3: Keep an array of alive turtles (name + coordinates) in the turtle_spawner node.
Publish this array on the /alive_turtles topic. On the turtle_controller node, subscribe to
the topic, get the array, and choose to select the first turtle on the array as the new
target.
Step 4: Create a service /catch_turtle in turtle_spawner. Once the turtle_controller has
reached a turtle, it will send the name of the turtle to that service. Then, from the
turtle_spawner node, call the /kill service , remove the turtle from the array, and publish
an updated array to /alive_turtles.
Step 5: Improve the turtle_controller to select the closest turtle instead of the first turtle
on the array.
Step 6: Add parameters and create a launch file.
