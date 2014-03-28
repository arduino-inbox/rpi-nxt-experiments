# coding=utf-8
"""
nxt-python example 1.
"""
from nxt import *

import nxt.locator

MIN_DISTANCE = 30

b = nxt.locator.find_one_brick()
print "brick:", b

u = Ultrasonic(b, PORT_4)
print "ultrasonic:", u

#l = Motor(b, PORT_B)
#r = Motor(b, PORT_C)
usm = Motor(b, PORT_A)

#m = SynchronizedMotors(l, r, 0)

while True:
    usm.turn(100, -20)
    d = u.get_distance()
    print "distance (left):", d
    usm.turn(100, 20)
    d = u.get_distance()
    print "distance (center):", d
    usm.turn(100, 20)
    d = u.get_distance()
    print "distance (right):", d
    usm.turn(100, -20)
    d = u.get_distance()
    print "distance (center):", d
    #if d < MIN_DISTANCE:
    #    m.turn(100, 360)
