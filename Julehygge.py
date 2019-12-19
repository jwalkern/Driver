import pigpio
import time

pi = pigpio.pi()

def tone(freq,duty):
       pi.set_PWM_frequency(12, freq)
       time.sleep(duty/1000)
       pi.set_PWM_frequency(12, 0)
       
def delay(num):
       time.sleep(num/1000)

c = 261
d = 293
e = 329
f = 349
g = 392


input('start')
#440 Hz er kammertone A4
pi.set_PWM_dutycycle(12, 128) #PWM 1/2 on

tone(e, 200)
tone(e, 200)
tone(e, 400)
tone(e, 200)
tone(e, 200)
tone(e, 400)
tone(e, 200)
tone(g, 200)
tone(c, 200)
tone(d, 200)
tone(e, 400)
delay(400)
tone(f, 200)
tone(f, 200)
tone(f, 200)
tone(f, 200)
tone(f, 200)
tone(e, 200)
tone(e, 200)
tone(e, 200)
tone(e, 200)
tone(d, 200)
tone(d, 200)
tone(e, 200)
tone(d, 200)
tone(g, 400)


pi.set_PWM_dutycycle(12, 0) #PWM off


input('stop')


