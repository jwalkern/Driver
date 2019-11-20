import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)

for index in range(2):
    input()
    test = GPIO.input(8)
    print(test)

count = 0
while count <= 10:
    trigger = GPIO.input(8)
    if trigger == 0:
        count = count + 1
        print("Du har trykket " + str(count) + " gange.")
        time.sleep(0.000010)




