#!/usr/bin/env python
import RPi.GPIO as GPIO

import time

BeepPin = 12   # pin12
LedPin = 7   #pin17

def setup():
	GPIO.setmode(GPIO.BOARD)        # Numbers pins by physical location
	GPIO.setup(BeepPin, GPIO.OUT)   # Set pin mode as output
	GPIO.output(BeepPin, GPIO.HIGH) # Set pin to high(+3.3V) to off the beep
	GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
	GPIO.output(LedPin, GPIO.HIGH) # Set pin to high(+3.3V) to off the beep
	
def loop():
	while True:
                print ('on')
                GPIO.output(LedPin, GPIO.LOW)  # led on
                GPIO.output(BeepPin, GPIO.LOW)
                time.sleep(0.5)
                print ('off')
                GPIO.output(LedPin, GPIO.HIGH)  # led off
                GPIO.output(BeepPin, GPIO.HIGH)
                time.sleep(0.5)
                
def destroy():
	GPIO.output(BeepPin, GPIO.HIGH)    # beep off
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	print ('Press Ctrl+C to end the program...')
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()


