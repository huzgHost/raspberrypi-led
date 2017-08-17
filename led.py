#!/usr/bin/python
# use bcm gpio

import RPi.GPIO as GPIO
import time

G = 14		# connect bcm 14
Y = 15		# connect bcm 15
R = 18		# connect bcm 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(G, GPIO.OUT)
#GPIO.setup(Y, GPIO.OUT)
#GPIO.setup(R, GPIO.OUT)

try:
	while True:
		t = 0.5
		GPIO.output(G, GPIO.HIGH)
		time.sleep(t)
		GPIO.output(G, GPIO.LOW)
		time.sleep(t)
	'''
	time.sleep(t)
	GPIO.output(R, GPIO.HIGH)
	time.sleep(t)
	'''

except KeyboardInterrupt:
	print 'Good by'

GPIO.cleanup()
