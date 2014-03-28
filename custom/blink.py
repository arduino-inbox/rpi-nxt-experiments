# coding=utf-8
"""
Blink example using my GPIO abstraction.
"""


from gpio import Gpio
from settings import LED
from time import sleep

gpio = Gpio()
pin = gpio.output(LED)

while True:
    pin.on()
    sleep(.5)
    pin.off()
    sleep(.5)
