import pigpio

pi = pigpio.pi()
pi.set_mode(32, pigpio.OUTPUT)

input('start')

pi.set_PWM_dutycycle(32, 128) #PWM 1/2 on
pi.set_PWM_frequency(32, 440 )

input('stop')

pi.set_PWM_dutycycle(32, 0) #PWM off
