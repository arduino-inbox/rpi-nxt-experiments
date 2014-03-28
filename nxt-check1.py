# coding=utf-8
"""
nxt-python example 1.
"""
from nxt import Motor, PORT_B, PORT_C, SynchronizedMotors

import nxt.locator
from time import sleep

b = nxt.locator.find_one_brick()
m_left = Motor(b, PORT_B)
m_right = Motor(b, PORT_C)
motors = SynchronizedMotors(m_left, m_right, 0)

while True:
    motors.turn(100, 360)
    m_left.turn(100, 360*4)

    sleep(.5)
