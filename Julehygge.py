import pigpio
import time

pi = pigpio.pi()
pi.set_mode(12, pigpio.OUTPUT)

input('start')

pi.set_PWM_dutycycle(12, 128) #PWM 1/2 on
pi.set_PWM_frequency(12, 440 ) #440 Hz er kammertone A4
time.sleep(1)
pi.set_PWM_frequency(12, 123)

input('stop')

pi.set_PWM_dutycycle(12, 0) #PWM off
