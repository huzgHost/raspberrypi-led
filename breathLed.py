#!/usr/bin/python
# use board gpio just change mode & switch G, Y , R

import RPi.GPIO as GPIO
import time

G = 8
Y = 10
R = 12

GPIO.setmode(GPIO.BOARD) # setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(R, GPIO.OUT)
GPIO.setup(Y, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)

'''
p = GPIO.PWM(G, 0.5)
p.start(1);
raw_input("stop by input")
p.stop()
GPIO.cleanup();
'''

g = GPIO.PWM(G, 50)
g.start(0)

r = GPIO.PWM(R, 50)
r.start(0)

try:
	while 1:
		# start:0, max:100, step:5
		for dc in range(0, 101, 5) :
			g.ChangeDutyCycle(dc)
			r.ChangeDutyCycle(dc)
			time.sleep(0.1)
		# start 100, min:0, step:-5
		for dc in range(100, -1, -5) :
			g.ChangeDutyCycle(dc)
			r.ChangeDutyCycle(dc)
			time.sleep(0.1)

except KeyboardInterrupt:
	pass

r.stop()
g.stop()
GPIO.cleanup()
