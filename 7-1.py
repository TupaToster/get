import RPi.GPIO as gpio
import matplotlib.pyplot as plt
import numpy as np
from time import *

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

gpio.setmode (gpio.BCM)
gpio.setup (dac, gpio.OUT)
gpio.setup (comp, gpio.IN)
gpio.setup (troyka, gpio.OUT)

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

values = []
expTime = time ()
cf = 3.3 / (2**8)

try:
    gpio.output (troyka, 0)
    while (True):
            val = adc (dac, comp)
            print (str (val) + " : " + str (val * cf))
            values.append (val)
            if (val * cf >= 2.7):
                break

    gpio.output (troyka, 1)

    while (True):
        val = adc (dac, comp)
        print (str (val) + " : " + str (val * cf))
        values.append (val)
        if (val * cf <= 0.9):
            break

finally:
    gpio.output (troyka, 0)
    expTime = time () - expTime
    
    with open ("data.txt", "w") as outF:
        for i in values:
            outF.write (str (i) + "\n")

    with open ("settings.txt", "w") as outF:
        outF.write ("Total time: " + str (expTime) + "\nOne measurement avg time: " + str (expTime / len (values)) + "\nDiscretization freq: " + str (len (values) / expTime) + "\nQuantovanie step adc: " + str (cf))

    x = np.linspace (0, expTime, len (values))

    plt.grid ()
    plt.plot (x, np.array (values) * cf, ".b")
    plt.show ()

    gpio.output (dac, gpio.LOW)
    gpio.output (troyka, gpio.HIGH)
    gpio.cleanup()