// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robot_interfaces:msg/TurtleArray.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACES__MSG__DETAIL__TURTLE_ARRAY__STRUCT_H_
#define ROBOT_INTERFACES__MSG__DETAIL__TURTLE_ARRAY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'turtles'
#include "robot_interfaces/msg/detail/turtle__struct.h"

/// Struct defined in msg/TurtleArray in the package robot_interfaces.
typedef struct robot_interfaces__msg__TurtleArray
{
  robot_interfaces__msg__Turtle__Sequence turtles;
} robot_interfaces__msg__TurtleArray;

// Struct for a sequence of robot_interfaces__msg__TurtleArray.
typedef struct robot_interfaces__msg__TurtleArray__Sequence
{
  robot_interfaces__msg__TurtleArray * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_interfaces__msg__TurtleArray__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOT_INTERFACES__MSG__DETAIL__TURTLE_ARRAY__STRUCT_H_
