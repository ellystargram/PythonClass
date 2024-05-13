import RPi.GPIO as GPIO
import time

trigerPin =23
echoPin=24
ledPin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)

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
		#distance unit is cm
		distance = pulse_duration * 17150
		print("Distance: %.2f cm" % distance)
		time.sleep(0.5)
except KeyboardInterrupt:
	GPIO.cleanup()
	print()
	print("exit...")