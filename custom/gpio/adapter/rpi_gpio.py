# coding=utf-8
"""
Rpi GPIO python library adapter package.
"""

from gpio.adapter import Engine
from RPi import GPIO


class RpiGpioEngine(Engine):
    """
    Rpi GPIO python library adapter.
    """

    def __init__(self):
        GPIO.setmode(GPIO.BCM)


    def input(self, pin_number):
        """
        Pin input setup method.
        @param pin_number: int
        """
        GPIO.setup(pin_number, GPIO.IN)

    def output(self, pin_number):
        """
        Pin output setup method.
        @param pin_number: int
        """
        GPIO.setup(pin_number, GPIO.OUT)

    def read(self, pin_number, pin_value):
        """
        Pin input read method.
        @param pin_number: int
        @param pin_value: int
        @return int
        """
        return int(GPIO.input(pin_number))

    def write(self, pin_number, pin_value):
        """
        Pin output write method.
        @param pin_number: int
        @param pin_value: int
        """
        GPIO.output(pin_number, pin_value)
