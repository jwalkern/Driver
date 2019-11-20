import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(8, GPIO.FALLING, bouncetime=200)

print("DO NOT PUSH THE BUTTON!")
count = 0
while count <= 9:
    if GPIO.event_detected(8):
        count = count + 1
        if count < 10:
            print("You have ignored the rule " + str(count) + " times.")
        else:
            print("That is it! BYE!")
        time.sleep(0.1)
GPIO.cleanup()







