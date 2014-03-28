# coding=utf-8
"""
Blink example using wiringPi2 python bindings.
"""

from wiringpi2 import GPIO
from settings import LED


io = GPIO(GPIO.WPI_MODE_PINS)
io.pinMode(LED, io.OUTPUT)

while True:
    io.digitalWrite(LED, io.HIGH)
    io.digitalWrite(LED, io.LOW)
