#!/usr/bin/env python

from susanoh.environments.gazebo_action import GazeboAction
import rospy
from geometry_msgs.msg import Twist
import numpy as np

rospy.init_node("random_walk")
target_name = ""
topic_name_vel = target_name+"/mobile_base/commands/velocity"
pub = rospy.Publisher(topic_name_vel, Twist, queue_size=10)
ga = GazeboAction()
rate = rospy.Rate(3)
while not rospy.is_shutdown():
    ga.control_action(np.random.randint(5))
    rate.sleep()
