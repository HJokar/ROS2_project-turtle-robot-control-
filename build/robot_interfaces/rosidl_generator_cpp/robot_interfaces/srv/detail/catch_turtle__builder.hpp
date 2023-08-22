// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_interfaces:srv/CatchTurtle.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACES__SRV__DETAIL__CATCH_TURTLE__BUILDER_HPP_
#define ROBOT_INTERFACES__SRV__DETAIL__CATCH_TURTLE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robot_interfaces/srv/detail/catch_turtle__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_CatchTurtle_Request_name
{
public:
  Init_CatchTurtle_Request_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robot_interfaces::srv::CatchTurtle_Request name(::robot_interfaces::srv::CatchTurtle_Request::_name_type arg)
  {
    msg_.name = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::srv::CatchTurtle_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::srv::CatchTurtle_Request>()
{
  return robot_interfaces::srv::builder::Init_CatchTurtle_Request_name();
}

}  // namespace robot_interfaces


namespace robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_CatchTurtle_Response_sucess
{
public:
  Init_CatchTurtle_Response_sucess()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robot_interfaces::srv::CatchTurtle_Response sucess(::robot_interfaces::srv::CatchTurtle_Response::_sucess_type arg)
  {
    msg_.sucess = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::srv::CatchTurtle_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::srv::CatchTurtle_Response>()
{
  return robot_interfaces::srv::builder::Init_CatchTurtle_Response_sucess();
}

}  // namespace robot_interfaces

#endif  // ROBOT_INTERFACES__SRV__DETAIL__CATCH_TURTLE__BUILDER_HPP_
