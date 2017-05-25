# ========================================= # Makers! Implement your own actions here. # =========================================
import RPi.GPIO as GPIO class GpioWrite(object):
'''Write the given value
to the given GPIO.'''
def __init__(self, gpio, value): GPIO.setmode(GPIO.BCM) GPIO.setup(gpio, GPIO.OUT) self.gpio = gpio
self.value = value
def run(self, command): GPIO.output(self.gpio, self.value)