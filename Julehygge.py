import pigpio
import time

pi = pigpio.pi()


buzzerPin = 12
tempo = 200 
notes = ["e","e","e","e","e","e","e","g","c","d","e"," ","f","f","f","f","f","e","e","e","e","d","d","e","d","g"]
duration = [1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2] 
def delay(ms):
       time.sleep(ms/1000)

def tone(buzzerPin, tone, duration):
       pi.set_PWM_frequency(buzzerPin, tone)
       delay(duration)
       pi.set_PWM_frequency(buzzerPin, 0)

def playTheShit(note, duration):
  notesName = [ 'c', 'd', 'e', 'f', 'g' ]
  tones = [ 261, 293, 329, 349, 392 ]

  for i in range(len(tones)):
         if note == notesName[i]:
                tone(buzzerPin, tones[i], duration)



input('start')
pi.set_PWM_dutycycle(12, 128) #PWM 1/2 on
for i in range(len(notes)):
       if notes[i] == " ":
              delay(duration[i] * tempo)
       else:
              playTheShit(notes[i], duration[i] * tempo)

       delay((tempo*2)*duration[i])

pi.set_PWM_dutycycle(12, 0) #PWM off

input('stop')


