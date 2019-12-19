import pigpio
import time

pi = pigpio.pi()
pi.set_mode(12, pigpio.OUTPUT)

highD = pi.set_PWM_frequency(12, 587)
midD = pi.set_PWM_frequency(12, 294)
midA = pi.set_PWM_frequency(12, 440)
midG = pi.set_PWM_frequency(12, 392)
midF = pi.set_PWM_frequency(12, 349)
midC = pi.set_PWM_frequency(12, 262)


input('start')
#440 Hz er kammertone A4
pi.set_PWM_dutycycle(12, 128) #PWM 1/2 on

midD
time.sleep(0.5)
midD
time.sleep(0.5)
highD
time.sleep(0.5)
midG
time.sleep(0.5)
midG
time.sleep(0.5)
midF
time.sleep(0.5)
midG
time.sleep(0.5)
midC
time.sleep(0.5)
midC
time.sleep(0.5)
highD
time.sleep(0.5)
midA
time.sleep(0.5)
midG
time.sleep(0.5)
midG
time.sleep(0.5)


input('stop')

pi.set_PWM_dutycycle(12, 0) #PWM off
