import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)
"""
for index in range(2):
    input()
    test = GPIO.input(8)
    print(test)
"""
print("DO NOT PUSH THE BUTTON!")
count = 0
while count <= 100:
    if GPIO.input(8) == 0 and check == True:
        count = count + 1
        if count <= 0 and count >10:
            print("I have told you " + str(count) + " times, not to push the button.")
        else:
            print("Why do I even try, you clearly don't care. Congrats you have pushed the button " + str(count) + " times.")
        #time.sleep(0.10)
        check = False
    if GPIO.input(8) == 1:
        check = True
GPIO.cleanup()





