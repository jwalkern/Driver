import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)

for index in range(2):
    input()
    test = GPIO.input(8)
    print(test)

check = True
count = 0
while count <= 10:
    if GPIO.input(8) == 0 and check == True:
        count = count + 1
        print("Du har trykket " + str(count) + " gange.")
        time.sleep(0.10)
        check = False
    check = True





