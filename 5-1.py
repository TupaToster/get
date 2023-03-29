import RPi.GPIO as gpio
from time import *

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

gpio.setmode (gpio.BCM)
gpio.setup (dac, gpio.OUT)
gpio.setup (comp, gpio.IN)
gpio.setup (troyka, gpio.OUT, initial = 0)

def dec2bin (val):
    return [int (i) for i in bin (val)[2:].zfill (len (dac))]

def adc (dac, comp):
    for i in range (2**8):
        gpio.output (dac, dec2bin (i))
        sleep (0.01)
        if (gpio.input (comp) == 0):
            gpio.output(dac, 0)
            return i
    return 2**8

try:
    while (True):
            sleep (0.01)
            print (str (adc(dac, comp)) + " : " + str (adc (dac, comp) / 2**8 *3.3))

finally:
    gpio.output (dac, gpio.LOW)
    gpio.output (troyka, gpio.LOW)
    gpio.cleanup()