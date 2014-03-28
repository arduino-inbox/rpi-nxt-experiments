# coding=utf-8
"""
GPIO libraries adapters.
"""
from gpio.adapter.rpi_gpio import RpiGpioEngine
from gpio.adapter.wiring2 import Wiring2Engine


class Driver(object):
    """
    GPIO libraries.
    """
    RPI_GPIO = "RPI_GPIO"
    WIRING2 = "WIRING2"


class Engine(object):
    """
    GPIO engine interface.
    """
    def input(self, pin_number):
        """
        Abstract pin input setup method.
        @param pin_number: int
        """
        raise NotImplemented

    def read(self, pin_number, pin_value):
        """
        Abstract pin input read method.
        @param pin_number: int
        @param pin_value: int
        """
        raise NotImplemented

    def output(self, pin_number):
        """
        Abstract pin output setup method.
        @param pin_number: int
        """
        raise NotImplemented

    def write(self, pin_number, pin_value):
        """
        Abstract pin output write method.
        @param pin_number: int
        @param pin_value: int
        """
        raise NotImplemented


class EngineFactory(object):
    @classmethod
    def create(cls, driver):
        if driver == Driver.RPI_GPIO:
            return RpiGpioEngine()
        elif driver == Driver.WIRING2:
            return Wiring2Engine()
