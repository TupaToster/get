import RPi.GPIO as gpio

dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setmode (gpio.BCM)
gpio.setup (dac, gpio.OUT)

def dec2bin (val):
    return [int (i) for i in bin (val)[2:].zfill (len (dac))]

try:
    while (True):
        print ("Input int in [0, 255]: ")
        val = input ()

        if (val[0] == 'q'):
            break
        try:
            val = float (val)
        except ValueError:
            print ("Input is not numerical")
            continue
        if (int (val) != float (val)):
            print ("float number got")
            continue
        elif (int (val) < 0):
            print ("Number less than zero")
            continue
        elif (int (val) > 255):
            print ("Number exceeds set limits towards up")
            continue

        val = int (val)

        print ("Expected voltage : " + str (val / 255 * 3.3) + " Volts")
        gpio.output (dac, dec2bin (val))

finally:
    gpio.output (dac, 0)
