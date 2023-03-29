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
            print (str (adc(dac, comp)) + " : " + str (adc (dac, comp) / 2**8 *3.3))

finally:
    gpio.output (dac, gpio.LOW)
    gpio.output (troyka, gpio.LOW)
    gpio.cleanup()