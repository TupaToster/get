import RPi.GPIO as gpio
from time import *

leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux =  [22, 23, 27, 18, 15, 14, 3, 2]

gpio.setmode (gpio.BCM)
gpio.setup (leds, gpio.OUT)
gpio.setup (aux, gpio.IN)


try:
    while True:
        for i in range (len (aux)):
            gpio.output (leds[i], gpio.input (aux[i]))
finally:
    gpio.output (leds, 0)
    gpio.cleanup ()