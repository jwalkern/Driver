import time
import serial

ser = serial.Serial(
        port = '/dev/ttyS0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

while True:
    data = input("Skriv noget her: ")
    ser.write(data.encode('UTF-8'))
    time.sleep(0.001)
    if data == 'quit':
        break