import pigpio
import time

pi = pigpio.pi()

def tone(pin,freq,duty):
       pi.set_PWM_frequency(pin, freq)
       time.sleep(duty/20000)
       pi.set_PWM_frequency(pin, 0)
       
def delay(num):
       time.sleep(num/20000)


input('start')
#440 Hz er kammertone A4
pi.set_PWM_dutycycle(12, 128) #PWM 1/2 on

tone( 12,294,125)  #D4
delay(125) 
tone( 12,294,125)  #D4
delay(125) 
tone( 12,587,250)  #D5
delay(250) 
tone( 12,440,250)  #A4
delay(375) 
tone( 12,415,125)  #Ab4
delay(250) 
tone( 12,392,250)  #G4
delay(250) 
tone( 12,349,250)  #F4
delay(250) 
tone( 12,294,125)  #D4
delay(125) 
tone( 12,349,125)  #F4
delay(125) 
tone( 12,392,125)  #G4
delay(125) 
tone( 12,261,125)  #C4(middle)     
delay(62) 
tone( 12,261,125)  #C4(middle)     
delay(62) 
tone( 12,261,125)  #C4(middle)     
delay(62) 
tone( 12,261,125)  #C4(middle)     
delay(62) 
tone( 12,587,250)  #D5
delay(250) 
tone( 12,440,375)  #A4
delay(375) 
tone( 12,415,125)  #Ab4
delay(250) 
tone( 12,392,250)  #G4
delay(250) 
tone( 12,349,250)  #F4
delay(250) 
tone( 12,294,125)  #D4
delay(125) 
tone( 12,349,125)  #F4
delay(125) 
tone( 12,392,125)  #G4
delay(125) 
tone( 12,247,125)  #B3
delay(125) 
tone( 12,247,125)  #B3
delay(125) 
tone( 12,587,250)  #D5
delay(250) 
tone( 12,440,375)  #A4
delay(375) 
tone( 12,415,125)  #Ab4
delay(250) 
tone( 12,392,250)  #G4
delay(250) 
tone( 12,349,250)  #F4
delay(250) 
tone( 12,294,125)  #D4
delay(125) 
tone( 12,349,125)  #F4
delay(125) 
tone( 12,392,125)  #G4
delay(125) 
tone( 12,233, 62)  #Bb3
delay(62) 
tone( 12,233, 62)  #Bb3
delay(62) 
tone( 12,233,62)  #Bb3
delay(62) 
tone( 12,233,62)  #Bb3
delay(62) 
tone( 12,587,250)  #D5
delay(250) 
tone( 12,440,375)  #A4
delay(375) 
tone( 12,415,125)  #Ab4
delay(250) 
tone( 12,392,250)  #G4
delay(250) 
tone( 12,349,250)  #F4
delay(250) 
tone( 12,294,125)  #D4
delay(125) 
tone( 12,349,125)  #F4
delay(125) 
tone( 12,392,125)  #G4
delay(125) 
tone( 12,294,125)  #D4
delay(125) 
tone( 12,294,125)  #D4
delay(125) 
tone( 12,587,250)  #D5
delay(250) 
tone( 12,440,375)  #A4
delay(375) 
tone( 12,415,125)  #Ab4
delay(250) 
tone( 12,392,250)  #G4
delay(250) 
tone( 12,349,250)  #F4
delay(250) 
tone( 12,294,125)  #D4
delay(125) 
tone( 12,349,125)  #F4
delay(125) 
tone( 12,392,125)  #G4
delay(125) 
tone( 12,261,125)  #C4(middle)     
delay(62) 
tone( 12,261,125)  #C4(middle)     
delay(62) 
tone( 12,261,125)  #C4(middle)     
delay(62) 
tone( 12,261,125)  #C4(middle)     
delay(62) 
tone( 12,587,250)  #D5
delay(250) 
tone( 12,440,375)  #A4
delay(375) 
tone( 12,415,125)  #Ab4
delay(250) 
tone( 12,392,250)  #G4
delay(250) 
tone( 12,349,250)  #F4
delay(250) 
tone( 12,294,125)  #D4
delay(125) 
tone( 12,349,125)  #F4
delay(125) 
tone( 12,392,125)  #G4
delay(125) 
tone( 12,247,125)  #B3
delay(125) 
tone( 12,247,125)  #B3
delay(125) 
tone( 12,587,250)  #D5
delay(250) 
tone( 12,440,375)  #A4
delay(375) 
tone( 12,415,125)  #Ab4
delay(250) 
tone( 12,392,250)  #G4
delay(250) 
tone( 12,349,250)  #F4
delay(250) 
tone( 12,294,125)  #D4
delay(125) 
tone( 12,349,125)  #F4
delay(125) 
tone( 12,392,125)  #G4
delay(125) 
tone( 12,233,62)  #Bb3
delay(62) 
tone( 12,233,62)  #Bb3
delay(62) 
tone( 12,233,62)  #Bb3
delay(62) 
tone( 12,233,62)  #Bb3
delay(62) 
tone( 12,588,250)  #D5
delay(250) 
tone( 12,440,375)  #A4
delay(375) 
tone( 12,415,125)  #Ab4
delay(250) 
tone( 12,392,250)  #G4
delay(250) 
tone( 12,349,250)  #F4
delay(250) 
tone( 12,294,125)  #D4
delay(125) 
tone( 12,349,125)  #F4
delay(125) 
tone( 12,392,125)  #G4
delay(125) 

input('stop')

pi.set_PWM_dutycycle(12, 0) #PWM off
