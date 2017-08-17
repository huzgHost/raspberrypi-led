#!/usr/bin/python
# timer led 

import RPi.GPIO as GPIO
import time



GREEN = 14
YELLOW = 15
RED = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)

def G():
	GPIO.output(GREEN, GPIO.HIGH)
	GPIO.output(YELLOW, GPIO.LOW)
	GPIO.output(RED, GPIO.LOW)
	return

def Y():
	GPIO.output(GREEN, GPIO.LOW)
	GPIO.output(YELLOW, GPIO.HIGH)
	GPIO.output(RED, GPIO.LOW)
	return

def R():
	GPIO.output(GREEN, GPIO.LOW)
	GPIO.output(YELLOW, GPIO.LOW)
	GPIO.output(RED, GPIO.HIGH)
	return

def close():
	GPIO.output(RED, GPIO.LOW)
	GPIO.output(GREEN, GPIO.LOW)
	GPIO.output(YELLOW, GPIO.LOW)

try:
	while(1):
		G();
		time.sleep(0.5);
		Y();
		time.sleep(0.5);
		R();
		time.sleep(0.5);

except KeyboardInterrupt:
	print ('Good bye')
	close()

GPIO.cleanup()
