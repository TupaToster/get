import RPi.GPIO as gpio

led = [24, 25, 8, 7, 12, 16, 20, 21]

gpio.setmode (gpio.BCM)
gpio.setup (led, gpio.OUT)

