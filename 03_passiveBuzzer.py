#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

BZRPin = 12
LedPin = 7   #pin17

GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
GPIO.setup(BZRPin, GPIO.OUT)   # Set pin mode as output
GPIO.output(BZRPin, GPIO.LOW)

GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
GPIO.output(LedPin, GPIO.HIGH) # Set pin to high(+3.3V) to off the beep

p = GPIO.PWM(BZRPin, 50) # init frequency: 50HZ
p.start(50)  # Duty cycle: 50%

try:
	while True:
		for f in range(100, 2000, 100):
			p.ChangeFrequency(f)
			GPIO.output(LedPin, GPIO.LOW)  # led on
			time.sleep(0.2)
		for f in range(2000, 100, -100):
			p.ChangeFrequency(f)
			GPIO.output(LedPin, GPIO.High)  # led off
			time.sleep(0.2)
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
