import RPi.GPIO as gpio
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setmode (gpio.BCM)
gpio.setup (dac, gpio.OUT)

def dec2bin (val):
    return [int (i) for i in bin (val)[2:].zfill (len (dac))]

try:
    while (True):
        for i in range (50, 256):
            gpio.output(dac, dec2bin (i))
            time.sleep ((2.0/205.0))
        
        for i in range (255, 49, -1):
            gpio.output (dac, dec2bin (i))
            time.sleep ((2.0 / 205.0))
finally:
    gpio.output (dac, 0)
