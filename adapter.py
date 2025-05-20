import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import Float64, Bool, String

class JoyProcessor(Node):
    def __init__(self):
        super().__init__('joy_processor')
        self.joy_sub = self.create_subscription(Joy, '/joy', self.joy_callback, 10)
        self.throttle_pub = self.create_publisher(Float64, '/throttle_command', 10)
        self.steering_pub = self.create_publisher(Float64, '/steering_command', 10)
        self.brake_pub = self.create_publisher(Float64, '/brake_command', 10)
        self.handbrake_pub = self.create_publisher(Bool, '/handbrake_command', 10)
        self.gear_pub = self.create_publisher(String, '/gear_command', 10)
        self.get_logger().info(f"Adapter initialized, waiting for Joy messages...")
        self.latest_joy = None
        self.first_joy_received = False

    def joy_callback(self, msg: Joy):
        if not self.first_joy_received:
            self.get_logger().info("Joy message received, adapter started!")
            self.first_joy_received = True
        self.latest_joy = msg
        
        # Process the Joy message and publish throttle and steering
        self.publish_throttle_and_steering(msg)

    def publish_throttle_and_steering(self, joy_msg: Joy):
        # Assuming axes[1] is throttle and axes[0] is steering
        throttle_value = (max(0.0, min(1.0, joy_msg.axes[2])))  # Clamp to [0.0, 1.0]
        steering_value = (max(-1.0, min(1.0, joy_msg.axes[0])))  # Clamp to [-1.0, 1.0]
        brake_value = (max(0.0, min(1.0, joy_msg.axes[3])))  # Clamp to [0.0, 1.0]

        # Publish throttle
        throttle_msg = Float64()
        throttle_msg.data = throttle_value
        self.throttle_pub.publish(throttle_msg)

        # Publish steering
        steering_msg = Float64()
        steering_msg.data = steering_value
        self.steering_pub.publish(steering_msg)
        
        # Publish braking
        brake_msg = Float64()
        brake_msg.data = brake_value
        self.brake_pub.publish(brake_msg)
        
        # Publish gear
        if joy_msg.buttons[4] == 1 or joy_msg.buttons[5] == 1:
            gear_msg = String()
            gear_msg.data = "reverse" if joy_msg.buttons[5] else "forward"
            self.gear_pub.publish(gear_msg)
        

def main(args=None):
    rclpy.init(args=args)
    node = JoyProcessor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
