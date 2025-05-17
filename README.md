# Simple-G29-CARLA-Adapter (Its only compatible with Xbox controller yet!!!)
I haven't been able to set it up for the Logitech G29 Steering Wheel, but I will do that shortly!!!
Its a simple ROS2 joy node based adapter for CARLA Simulator that translates the Logitech G29 steering wheel's steering, throttle and brake into data that CARLA understands, there is no force feedback or anything. You also need [Joy](https://github.com/ros-drivers/joystick_drivers/tree/ros2/joy) to run it

How to use it:

Go into your ROS2 workspace's src folder and clone the repository (This code assumes its 'ros2_ws')

`cd ros2_ws/src/`

`git clone https://github.com/Fishir88/Simple-G29-CARLA-Adapter.git`

```cd ..
colcon build --symlink-install --packages-select g29_adapter```

`source ~/ros2_ws/install/setup.bash`

Run the Joy package's joy_node
`ros2 run joy joy_node`

`ros2 run g29_adapter adapter`
