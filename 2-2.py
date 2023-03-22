import RPi.GPIO as gpio
from time import *

dac = [26, 19, 13, 6, 5, 11, 9, 10]

def dec2bin (val):
    return [int (i) for i in bin (val)[2:].zfill (len (dac))]

gpio.setmode (gpio.BCM)
gpio.setup (dac, gpio.OUT)

try:
    while True:
        i = int(input ())
        if i == -1:
            break
        gpio.output (dac, dec2bin (i))
finally:
    gpio.output (dac, 0)
    gpio.cleanup ()
