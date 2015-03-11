#!/usr/bin/env python
import roslib; roslib.load_manifest('example_1')
import rospy
import math

from std_msgs.msg import String
from turtlesim.srv import TeleportRelative
from geometry_msgs.msg import Twist

K_ANGLE=15
K_SPEED=4

def talker():
    rospy.init_node('turtle1_go')
    serv1=rospy.ServiceProxy('turtle1/teleport_relative',TeleportRelative)
    while not rospy.is_shutdown():
       if rospy.get_param("example_1/start")==1:
          joy_tek=rospy.get_param("example_1/joy_tek")
          speed=joy_tek[1]/K_SPEED
          k=1
          if joy_tek[1]<0:
            k=-1
          angle=math.asin(joy_tek[0]*k)/K_ANGLE
          res1=serv1(speed,angle);
       rospy.sleep(0.1)
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass

