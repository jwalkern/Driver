import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.IN)


def måleafstand():
    GPIO.output(8, True)
    time.sleep(0.00001)
    GPIO.output(8, False)

    while GPIO.input(10) == 0:
        startTime = time.time()

    while GPIO.input(10) == 1:
        stopTime = time.time()

    tid = stopTime - startTime
    afstand = (tid * 34300) / 2
    return afstand


input("tryk 'enter' for at måle afstand.")

dist = måleafstand()
print("Den målte afstand er = %.1f cm" % dist)
time.sleep(1)

input("tryk 'enter' for at afslutte.")

GPIO.cleanup()