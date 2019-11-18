from sensorHCSR04 import distance

input("tryk 'enter' for at måle afstand.")

dist = distance()
print("Den målte afstand er = %.1f cm" % dist)
time.sleep(1)
