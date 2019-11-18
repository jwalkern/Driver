from sensorHCSR04 import distance
import RPi.GPIO as GPIO

input("tryk 'enter' for at måle afstand.")
dist = distance()
print("Den målte afstand er = %.1f cm" % dist)
GPIO.cleanup()
