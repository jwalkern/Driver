import pigpio
import time

pi = pigpio.pi()
pi.set_mode(12, pigpio.OUTPUT)

def tone(num):
       pi.set_PWM_frequency(12, num)


midD = 294
highD = 587
midA = 440
midG = 392
midF = 349
midC = 262

input('start')
#440 Hz er kammertone A4
pi.set_PWM_dutycycle(12, 128) #PWM 1/2 on

tone(midD)
time.sleep(0.5)
tone(midD)
time.sleep(0.5)
tone(highD)
time.sleep(0.5)
tone(midG)
time.sleep(0.5)
tone(midG)
time.sleep(0.5)
tone(midF)
time.sleep(0.5)
tone(midG)
time.sleep(0.5)
tone(midC)
time.sleep(0.5)
tone(midC)
time.sleep(0.5)
tone(highD)
time.sleep(0.5)
tone(midA)
time.sleep(0.5)
tone(midG)
time.sleep(0.5)
tone(midG)
time.sleep(0.5)


input('stop')

pi.set_PWM_dutycycle(12, 0) #PWM off
