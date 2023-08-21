// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_interfaces:msg/Turtle.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACES__MSG__DETAIL__TURTLE__BUILDER_HPP_
#define ROBOT_INTERFACES__MSG__DETAIL__TURTLE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robot_interfaces/msg/detail/turtle__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robot_interfaces
{

namespace msg
{

namespace builder
{

class Init_Turtle_name
{
public:
  explicit Init_Turtle_name(::robot_interfaces::msg::Turtle & msg)
  : msg_(msg)
  {}
  ::robot_interfaces::msg::Turtle name(::robot_interfaces::msg::Turtle::_name_type arg)
  {
    msg_.name = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::msg::Turtle msg_;
};

class Init_Turtle_theta
{
public:
  explicit Init_Turtle_theta(::robot_interfaces::msg::Turtle & msg)
  : msg_(msg)
  {}
  Init_Turtle_name theta(::robot_interfaces::msg::Turtle::_theta_type arg)
  {
    msg_.theta = std::move(arg);
    return Init_Turtle_name(msg_);
  }

private:
  ::robot_interfaces::msg::Turtle msg_;
};

class Init_Turtle_y
{
public:
  explicit Init_Turtle_y(::robot_interfaces::msg::Turtle & msg)
  : msg_(msg)
  {}
  Init_Turtle_theta y(::robot_interfaces::msg::Turtle::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_Turtle_theta(msg_);
  }

private:
  ::robot_interfaces::msg::Turtle msg_;
};

class Init_Turtle_x
{
public:
  Init_Turtle_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Turtle_y x(::robot_interfaces::msg::Turtle::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_Turtle_y(msg_);
  }

private:
  ::robot_interfaces::msg::Turtle msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::msg::Turtle>()
{
  return robot_interfaces::msg::builder::Init_Turtle_x();
}

}  // namespace robot_interfaces

#endif  // ROBOT_INTERFACES__MSG__DETAIL__TURTLE__BUILDER_HPP_
