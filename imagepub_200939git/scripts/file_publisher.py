#!/usr/bin/env python

import rospy
from rospy.numpy_msg import numpy_msg
import cv2 as cv
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

def file_publisher():
        pub = rospy.Publisher("image", Image, queue_size= 10)
        rospy.init_node("file_publisher",anonymous=True)
        
        path = "/home/shivams/Downloads/checkerboard.jpg"
        frequency = rospy.set_param("frequency",10)
        
        img = cv.imread(path)
        bridge = CvBridge()
        image_message = bridge.cv2_to_imgmsg(img,encoding="passthrough")
        
        rate = rospy.Rate(frequency)

        while not rospy.is_shutdown():
            pub.publish(image_message)
            rate.sleep()

if __name__ == '__main__':
    try:
        file_publisher()
    except rospy.ROSInterruptException:
        pass
        