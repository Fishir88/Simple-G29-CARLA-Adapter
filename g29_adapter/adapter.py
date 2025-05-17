import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import Float64

class JoyProcessor(Node):
    def __init__(self):
        super().__init__('joy_processor')
        self.joy_sub = self.create_subscription(Joy, '/joy', self.joy_callback, 10)
        
        # Publishers for throttle and steering and braking
        self.throttle_pub = self.create_publisher(Float64, '/throttle_command', 10)
        self.steering_pub = self.create_publisher(Float64, '/steering_command', 10)
        self.brake_pub = self.create_publisher(Float64, '/brake_command', 10)
        
        self.latest_joy = None

    def joy_callback(self, msg: Joy):
        self.latest_joy = msg
        self.get_logger().info(f"Received Joy message: axes={msg.axes}, buttons={msg.buttons}")
        
        # Process the Joy message and publish throttle and steering
        self.publish_throttle_and_steering(msg)

    def publish_throttle_and_steering(self, joy_msg: Joy):
        # Assuming axes[1] is throttle and axes[0] is steering
        throttle_value = -(max(0.0, min(1.0, joy_msg.axes[4])))  # Clamp to [0.0, 1.0]
        steering_value = -(max(-1.0, min(1.0, joy_msg.axes[0])))  # Clamp to [-1.0, 1.0]
        brake_value = -(max(0.0, min(1.0, joy_msg.buttons[5])))  # Clamp to [0.0, 1.0]

        # Publish throttle
        throttle_msg = Float64()
        throttle_msg.data = throttle_value
        self.throttle_pub.publish(throttle_msg)
        self.get_logger().info(f"Published throttle: {throttle_msg}")

        # Publish steering
        steering_msg = Float64()
        steering_msg.data = steering_value
        self.steering_pub.publish(steering_msg)
        self.get_logger().info(f"Published steering: {steering_msg}")
        
        # Publish braking
        brake_msg = Float64()
        brake_msg.data = brake_value
        self.brake_pub.publish(brake_msg)
        self.get_logger().info(f"Published brake: {brake_msg}")

def main(args=None):
    rclpy.init(args=args)
    node = JoyProcessor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
