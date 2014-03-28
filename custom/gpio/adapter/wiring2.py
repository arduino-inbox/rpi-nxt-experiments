# coding=utf-8
"""
Wiring2 python bindings adapter package.
"""

from gpio.adapter import Engine
from wiringpi2 import GPIO

class Wiring2Engine(Engine):
    """
    Wiring2 python bindings adapter.
    """

    def __init__(self):
        self._io = GPIO(GPIO.WPI_MODE_PINS)

    def input(self, pin_number):
        """
        Pin input setup method.
        @param pin_number: int
        """
        self._io.pinMode(pin_number, self._io.INPUT)

    def output(self, pin_number):
        """
        Pin output setup method.
        @param pin_number: int
        """
        self._io.pinMode(pin_number, self._io.OUTPUT)

    def read(self, pin_number, pin_value):
        """
        Pin input read method.
        @param pin_number: int
        @param pin_value: int
        @return int
        """
        return int(self._io.digitalRead(pin_number))

    def write(self, pin_number, pin_value):
        """
        Pin output write method.
        @param pin_number: int
        @param pin_value: int
        """
        self._io.digitalWrite(pin_number, pin_value)
