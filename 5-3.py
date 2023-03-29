import RPi.GPIO as gpio
from time import *
import math

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [24, 25, 8, 7, 12, 16, 20, 21]
comp = 4
troyka = 17

gpio.setmode (gpio.BCM)
gpio.setup (dac, gpio.OUT)
gpio.setup (comp, gpio.IN)
gpio.setup (troyka, gpio.OUT, initial = 0)
gpio.setup (leds, gpio.OUT)

def dec2bin (val):
    return [int (i) for i in bin (val)[2:].zfill (len (dac))]

def adc (dac, comp):
    output = [0] * 8
    for i in range (8):
        output[i] = 1
        gpio.output(dac, output)
        sleep (0.01)
        if (gpio.input (comp) == 0): output[i] = 0
    out = 0
    for i in range (8):
        out += output[i] * (2**(7 - i))
    return out

try:
    while (True):
            sleep (0.01)
            volume = [0] * 8
            for i in range (round (adc (dac, comp) / 255 * 8)):
                volume[i] = 1
            gpio.output(leds, volume)

finally:
    gpio.output (dac, gpio.LOW)
    gpio.output (troyka, gpio.LOW)
    gpio.cleanup()