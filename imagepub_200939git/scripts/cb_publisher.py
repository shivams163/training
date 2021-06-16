#!/usr/bin/env python

import rospy
import numpy as np
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats
import std_msgs.msg

def cb_publisher():
    
        height = rospy.set_param("height",64.0)
        width = rospy.get_param("width",64.0)
        squaresize = rospy.get_param("square_size",8.0)
        frequency = rospy.get_param("frequency",10)
        pub = rospy.Publisher("cb_img", numpy_msg(Floats), queue_size= 10)
        rospy.init_node("cb_publisher",anonymous=True)
        

        

        rate = rospy.Rate(frequency)

        # data_to_send = std_msgs.msg.Float64MultiArray()
        # data_to_send.data = a

        while not rospy.is_shutdown():
            a = np.zeros((height,width))
            for i in range(height//squaresize):
                for j in range(width//squaresize):
                    for k in range(squaresize):
                        for l in range(squaresize):
                            if (i+j)%2==0:
                                a[i*squaresize+k][j*squaresize+l]=1
            pub.publish(a)
            rate.sleep()

if __name__ == '__main__':
    try:
        cb_publisher()
    except rospy.ROSInterruptException:
        pass