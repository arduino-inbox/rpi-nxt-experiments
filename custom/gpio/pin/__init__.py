# coding=utf-8
"""
GPIO pin abstractions.
"""


class PinMode(object):
    """
    GPIO pin modes enum.
    """
    INPUT = 1
    OUTPUT = 0


class PinValue(object):
    """
    GPIO pin values enum.
    """
    HIGH = 1
    LOW = 0


class Pin(object):
    """
    GPIO pin.
    """
    def __init__(self, gpio, pin_number, pin_mode,
                 pin_value=PinValue.LOW):
        """
        Initialize pin with a given GPIO pin number and mode.
        @param pin_number: int
        @param pin_mode: int
        """
        self.number = pin_number
        self.mode = pin_mode
        self.value = pin_value
        self.gpio = gpio
        self.gpio.pins.append(self)


class OutputPin(Pin):
    """
    GPIO Output pin.
    @param pin_number: int
    """
    def __init__(self, gpio, pin_number):
        super(OutputPin, self).__init__(gpio, pin_number, PinMode.OUTPUT)
        self.gpio.output_pins.append(self)
        self.gpio.engine.output(pin_number)

    def on(self):
        """
        Turn on the pin.
        """
        self.value = PinValue.HIGH
        self.gpio.update()

    def off(self):
        """
        Turn off the pin.
        """
        self.value = PinValue.HIGH
        self.gpio.update()


class InputPin(Pin):
    """
    GPIO Input pin.
    @param pin_number: int
    """
    def __init__(self, gpio, pin_number):
        super(InputPin, self).__init__(gpio, pin_number, PinMode.INPUT)
        self.gpio.input_pins.append(self)
        self.gpio.engine.input(pin_number)
