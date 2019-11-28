import serial
import lcd_skærm as l
import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.cleanup()
foo = serial.Serial(port='/dev/ttyS0', timeout=1)
l.init_display(21, 20, [6,13,19,26], 0, 0)


while True:
    x = foo.readline()
    l.write_string(x.decode('UTF-8'))
    if x.decode('UTF-8') == 'clear':
        l.clear_display()
    elif x.decode('UTF-8') == 'quit':
        l.clear_display()
        l.write_string('goodbye')
        time.sleep(2)
        l.clear_display()
        break
    
gpio.cleanup()