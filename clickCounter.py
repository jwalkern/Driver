import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("DO NOT PUSH THE BUTTON!")
count = 0
while count <= 49:
    if GPIO.input(8) == 0 and check == True:
        count = count + 1
        if count < 50:
            print("You have ignored the rule " + str(count) + " times.")
        else:
            count == 50
            print("That is it! BYE!")
        check = False
        time.sleep(0.1)
    if GPIO.input(8) == 1:
        check = True
GPIO.cleanup()







