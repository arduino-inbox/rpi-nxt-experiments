# coding=utf-8
"""
GPIO abstractions.
"""
from gpio.adapter import Driver, EngineFactory
from gpio.pin import OutputPin, InputPin


class Gpio(object):
    """
    GPIO engine.
    """
    def __init__(self, driver=Driver.RPI_GPIO):
        self.pins = []
        self.input_pins = []
        self.output_pins = []
        self.driver = driver
        self.engine = EngineFactory.create(self.driver)

    def output(self, pin_number):
        """
        Output pin factory method.

        @param pin_number: int
        @return: OutputPin
        """
        return OutputPin(self, pin_number)

    def input(self, pin_number):
        """
        Input pin factory method.

        @param pin_number: int
        @return: InputPin
        """
        return InputPin(self, pin_number)

    def update(self):
        """
        Update pins.
        """
        for output_pin in self.output_pins:
            self._write(output_pin)
        for input_pin in self.input_pins:
            self._read(input_pin)

    def _write(self, output_pin):
        """
        Write value to output pin
        @param output_pin: OutputPin
        """
        self.engine.write(output_pin.number, output_pin.value)

    def _read(self, input_pin):
        """
        Read value from input pin
        @param input_pin: InputPin
        """
        self.engine.read(input_pin.number, input_pin.value)
