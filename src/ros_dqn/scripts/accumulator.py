#!/usr/bin/env python                                                                 

import rospy
from std_msgs.msg import Int16

from susanoh.environments.gazebo_action import GazeboAction
import numpy as np

topic_name = "accumulator"
rospy.init_node(topic_name)

target_name = ""
topic_name_vel = target_name+"/mobile_base/commands/velocity"



ga = GazeboAction()

class Accumulator(object):
    def __init__(self):
        self.accumulators = [0, 0, 0, 0, 0]
        self.act_id = 0

    def __call__(self, message):
        self.accumulators[message.data] += 0.5
        rospy.loginfo("Message : %s", str(message.data))
        if self.accumulators[message.data] >= 1.0:
            self.accumulators = [0, 0, 0, 0, 0]
            self.act_id = message.data
            
accumulator = Accumulator()
sub = rospy.Subscriber("rand_act", Int16, accumulator)

rate = rospy.Rate(3)
while not rospy.is_shutdown():
    ga.control_action(accumulator.act_id)
    rate.sleep()
