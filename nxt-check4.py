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

l = Motor(b, PORT_B)
r = Motor(b, PORT_C)
m = SynchronizedMotors(l, r, 0)

usm = Motor(b, PORT_A)

while True:
    usm.turn(100, -20)
    print "distance (left):", u.get_distance()
    print "tacho (left):", usm.get_tacho()

    usm.turn(100, 20)
    print "distance (center):", u.get_distance()
    print "tacho (center):", usm.get_tacho()

    usm.turn(100, 20)
    print "distance (right):", u.get_distance()
    print "tacho (right):", usm.get_tacho()

    usm.turn(100, -20)
    print "distance (center):", u.get_distance()
    print "tacho (center):", usm.get_tacho()

    #if d < MIN_DISTANCE:
    #    m.turn(100, 360)
