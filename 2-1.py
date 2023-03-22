import RPi.GPIO as gpio
from time import *

led = [24, 25, 8, 7, 12, 16, 20, 21]

gpio.setmode (gpio.BCM)
gpio.setup (led, gpio.OUT)

for i in range (3):
    for i in led:
        gpio.output(i, 1)
        sleep (0.2)
        gpio.output(i, 0)
        sleep (0.2)

gpio.output (led, 0)

gpio.cleanup()