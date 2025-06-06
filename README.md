# Simple-G29-CARLA-Adapter
Its a simple ROS2 joy node based adapter for CARLA Simulator that translates the Logitech G29 steering wheel's steering, throttle and brake into data that CARLA understands, you will have to switch your G29 to PS3 mode so there is no force feedback, centering or anything motorized. You will also need [Joy](https://github.com/ros-drivers/joystick_drivers/tree/ros2/joy) to run it

Additional useful information: To select gears (forward and backward), you can use the paddles on the back. The right one sets it to "forward" and the left one sets it to "backward".

How to use it:

Go into your ROS2 workspace's src folder and clone the repository (This code assumes its 'ros2_ws')

```
cd ~/ros2_ws/src/
```

```
git clone https://github.com/Fishir88/Simple-G29-CARLA-Adapter.git
```

```
cd ~/ros2_ws
colcon build --symlink-install --packages-select g29_adapter
```

```
source ~/ros2_ws/install/setup.bash
```

Run the Joy package's joy_node in a different terminal
`ros2 run joy joy_node`


```
ros2 run g29_adapter adapter
```
If everything works well, you should get these messages:

"Adapter initialized, waiting for Joy messages..."

"Joy message received, adapter started!"
