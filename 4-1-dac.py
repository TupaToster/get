import RPi.GPIO as gpio
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setmode (gpio.BCM)
gpio.setup (dac, gpio.out)

def dec2bin (val):
    return [int (i) for i in bin (val)[2:].zfill (len (dac))]

try:
    while (True):
        print ("Input int in [0, 255] : ")
        val = int (input ())
        if (val < 0 or val > 255) continue
        print ("Expected voltage : " + str (val / 255 * 3.3))
        gpio.output (dac, dec2bin (val))
finally:
    gpio.output (dac, [0]*len(dac))
