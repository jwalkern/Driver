import RPi.GPIO as GPIO
import time

_HCSR04_sensor_trigger = None
_HCSR04_sensor_echo = None


def init(sensor_trigger = 8, sensor_echo = 10):
    #set GPIO pins
    global _HCSR04_sensor_echo, _HCSR04_sensor_trigger
    _HCSR04_sensor_trigger = sensor_trigger
    _HCSR04_sensor_echo = sensor_echo

    #set GPIO mode (GPIO.BOARD)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(sensor_trigger, GPIO.OUT)
    GPIO.setup(sensor_echo, GPIO.IN)


def distance():
    global _HCSR04_sensor_echo, _HCSR04_sensor_trigger
    startTime = time.time()
    stopTime = time.time()

    #set trigger high and low after 20ms
    GPIO.output(_HCSR04_sensor_trigger, True)
    time.sleep(0.00002)
    GPIO.output(_HCSR04_sensor_trigger, False)

    #Mesure the start and stop time
    while GPIO.input(_HCSR04_sensor_echo) == 0:
        startTime = time.time()
    while GPIO.input(_HCSR04_sensor_echo) == 1:
        stopTime = time.time()

    #Time difference
    timeElapsed = stopTime - startTime
    #calc the distantce
    distance = (timeElapsed * 34300) / 2
    return distance



