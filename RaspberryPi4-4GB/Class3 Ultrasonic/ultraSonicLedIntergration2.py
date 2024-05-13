import RPi._GPIO as GPIO
import time

trigerPin = 23
echoPin = 24
led1Pin = 18
led2Pin = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigerPin, GPIO.OUT)
GPIO.setup(led1Pin, GPIO.OUT)
GPIO.setup(led2Pin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

GPIO.output(trigerPin, GPIO.LOW)

try:
	while True:
		GPIO.output(trigerPin, GPIO.HIGH)
		time.sleep(0.00001)
		GPIO.output(trigerPin, GPIO.LOW)
		while not GPIO.input(echoPin):
			pulse_start = time.time()
		while GPIO.input(echoPin):
			pulse_end = time.time()
		pulse_duration = pulse_end - pulse_start
		distance = pulse_duration * 17150
		print("Distance: %.2f cm" % distance)
		if distance < 10:
			GPIO.output(led1Pin, GPIO.HIGH)
			GPIO.output(led2Pin, GPIO.LOW)
		else:
			GPIO.output(led1Pin, GPIO.LOW)
			GPIO.output(led2Pin, GPIO.HIGH)
		time.sleep(0.5)
except:
	GPIO.cleanup()
	print()
	print("jongryo...")