// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robot_interfaces:msg/Turtle.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACES__MSG__DETAIL__TURTLE__STRUCT_H_
#define ROBOT_INTERFACES__MSG__DETAIL__TURTLE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'name'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/Turtle in the package robot_interfaces.
typedef struct robot_interfaces__msg__Turtle
{
  double x;
  double y;
  double theta;
  rosidl_runtime_c__String name;
} robot_interfaces__msg__Turtle;

// Struct for a sequence of robot_interfaces__msg__Turtle.
typedef struct robot_interfaces__msg__Turtle__Sequence
{
  robot_interfaces__msg__Turtle * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_interfaces__msg__Turtle__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOT_INTERFACES__MSG__DETAIL__TURTLE__STRUCT_H_
