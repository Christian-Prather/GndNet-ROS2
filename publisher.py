import rclpy
from rclpy.node import Node
from utils.ros_utils import np2ros_pub_2, gnd_marker_pub
from sensor_msgs.msg import PointCloud2
from visualization_msgs.msg import Marker
rclpy.init()


class MainPublisher(Node):
    def __init__(self):
        super().__init__("Gnd_Publisher")
        self.pcl_publisher_ = self.create_publisher(
            PointCloud2, '/kitti/velo/pointcloud', 10)
        self.marker_publisher_ = self.create_publisher(
            Marker, '/kitti/gnd_marker_pred', 10)
