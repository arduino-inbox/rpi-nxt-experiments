# coding=utf-8
"""
Blink example using RPi.GPIO python package.
"""

from RPi import GPIO
from settings import LED


GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

while True:
    GPIO.output(LED, True)
    GPIO.output(LED, False)