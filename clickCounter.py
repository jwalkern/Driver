import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)

print("DO NOT PUSH THE BUTTON!")
count = 0
while count <= 99:
    if GPIO.input(8) == 0 and check == True:
        count = count + 1
        print("You have ignored the rule " + str(count) + " times.")
        #time.sleep(0.10)
        check = False
    if GPIO.input(8) == 1:
        check = True
GPIO.cleanup()





