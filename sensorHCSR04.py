import RPi.GPIO as GPIO
import time

#set GPIO pins
sensor_trigger = 8
sensor_echo = 10

#set GPIO mode (GPIO.BOARD)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor_trigger, GPIO.OUT)
GPIO.setup(sensor_echo, GPIO.IN)


def distance():
    startTime = time.time()
    stopTime = time.time()

    GPIO.output(sensor_trigger, True)
    time.sleep(0.00002)
    GPIO.output(sensor_trigger, False)


    #Mesure the start and stop time
    while GPIO.input(sensor_echo) == 0:
        startTime = time.time()

    while GPIO.input(sensor_echo) == 1:
        stopTime = time.time()
    #Time differ
    timeElapsed = stopTime - startTime
    distance = (timeElapsed * 34300) / 2
    return distance


input("tryk 'enter' for at måle afstand.")

dist = måleafstand()
print("Den målte afstand er = %.1f cm" % dist)
time.sleep(1)

input("tryk 'enter' for at afslutte.")

GPIO.cleanup()