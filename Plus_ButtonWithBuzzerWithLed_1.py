#!/usr/bin/env python
import RPi.GPIO as GPIO

LedPin = 7    # pin11 --- led
BtnPin = 40    # pin40 --- button
BeepPin = 12   # pin12

Led_status = 1

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
	GPIO.setup(BeepPin, GPIO.OUT)   # Set pin mode as output
	GPIO.output(BeepPin, GPIO.HIGH) # Set pin to high(+3.3V) to off the beep
	GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to make led off

def swLed(ev=None):
	global Led_status
	Led_status = not Led_status
	GPIO.output(LedPin, Led_status)  # switch led status(on-->off; off-->on)
	GPIO.output(BeepPin, Led_status)  # switch buzzer status(on-->off; off-->on)
	if Led_status == 1:
		print ('led off...')
	else:
		print ('...led on')

def loop():
	GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=swLed) # wait for falling
	while True:
		pass   # Don't do anything

def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()


