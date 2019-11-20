import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)

for index in range(4):
    input()
    test = GPIO.input(8)
    print(test)





