import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)

print("DO NOT PUSH THE BUTTON!")
count = 0
while count <= 99:
    if GPIO.input(8) == 0 and check == True:
        count = count + 1
        if count < 98:
            print("You have ignored the rule " + str(count) + " times.")
        else:
            print("That is it! BYE!")
        check = False
    if GPIO.input(8) == 1:
        check = True
GPIO.cleanup()





