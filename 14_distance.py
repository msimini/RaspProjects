#! /usr/bin/python
import RPi.GPIO as GPIO
import time

def checkdist():
	GPIO.output(31, GPIO.HIGH)
	time.sleep(0.000015)
	GPIO.output(31, GPIO.LOW)
	while not GPIO.input(29):
		pass
	t1 = time.time()
	while GPIO.input(29):
		pass
	t2 = time.time()
	return (t2-t1)*340/2

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(29,GPIO.IN)
time.sleep(2)
try:
	while True:
		print ('Distance: %0.2f m' %checkdist())
		time.sleep(0.5)
except KeyboardInterrupt:
	GPIO.cleanup()


