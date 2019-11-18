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

    #set trigger high and low after 20ms
    GPIO.output(sensor_trigger, True)
    time.sleep(0.00002)
    GPIO.output(sensor_trigger, False)

    #Mesure the start and stop time
    while GPIO.input(sensor_echo) == 0:
        startTime = time.time()
    while GPIO.input(sensor_echo) == 1:
        stopTime = time.time()

    #Time difference
    timeElapsed = stopTime - startTime
    #calc the distantce
    distance = (timeElapsed * 34300) / 2
    return distance
    GPIO.cleanup()

input("tryk 'enter' for at måle afstand.")

dist = distance()
print("Den målte afstand er = %.1f cm" % dist)
time.sleep(1)
