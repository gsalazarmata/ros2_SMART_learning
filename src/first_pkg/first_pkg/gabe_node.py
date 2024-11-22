import rclpy
from rclpy.node import Node

class MyNode(Node):
    
    def __init__(self):
        super().__init__("name_node")
        self.counter_ = 0
        self.get_logger().info("Hello Gabe")
        self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info("Hello Gabe is AWESOME " + str(self.counter_))
        # self.get_logger().info("Hello Gabe")

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()