from sensorHCSR04 import distance
from sensorHCSR04 import init
import RPi.GPIO as GPIO

init(8,10)
input("tryk 'enter' for at måle afstand.")
dist = distance()
print("Den målte afstand er = %.1f cm" % dist)
GPIO.cleanup()
