# coding=utf-8
"""
nxt-python example 1.
"""
from nxt import Motor, PORT_B, PORT_C, SynchronizedMotors, Ultrasonic, PORT_4

import nxt.locator

MIN_DISTANCE = 30

b = nxt.locator.find_one_brick()
print "brick:", b

u = Ultrasonic(b, PORT_4)
print "ultrasonic:", u

l = Motor(b, PORT_B)
r = Motor(b, PORT_C)
m = SynchronizedMotors(l, r, 0)

while True:
    d = u.get_distance()
    print "distance:", d
    if d < MIN_DISTANCE:
        m.turn(100, 360)
