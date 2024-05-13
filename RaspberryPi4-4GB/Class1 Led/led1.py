import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
ledPin = 23
GPIO.setup(ledPin, GPIO.OUT)

while True:
	GPIO.output(ledPin, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(ledPin, GPIO.LOW)
	time.sleep(1)
 
 