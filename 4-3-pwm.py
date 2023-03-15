import RPi.GPIO as gpio

dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setmode (gpio.BCM)
gpio.setup (dac, gpio.OUT)

def dec2bin (val):
    return [int (i) for i in bin (val)[2:].zfill (len (dac))]

gpio.setmode (gpio.BCM)
gpio.setup (24, gpio.OUT)
gpio.setup (18, gpio.OUT)

pin = gpio.PWM(24, 100)
pin1 = gpio.PWM (18, 100)
pin.start(0)
pin1.start (0)

try:
    while (True):
        a = float (input ("Give me pls duty cicle in percent : "))
        print ("Expected voltage (if herz is high) : " + str (3.3 * min (100, a) / 100.0))
        pin.start (min (100, a))
        pin1.start (min (100, a))
        gpio.output (dac, dec2bin (int (min (100, int (a)) * 255 / 100)))
finally:
    gpio.cleanup ()

    


