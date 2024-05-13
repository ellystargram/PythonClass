import RPi.GPIO as GPIO
import time

led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
led_pwm=GPIO.PWM(led_pin, 100)
led_pwm.start(0)

try:
	while True:
		userInput = input("Enter a brightness percentage (0, 5, f): ")
		if userInput == 'f':
			led_pwm.ChangeDutyCycle(100)
		elif userInput == '5':
			led_pwm.ChangeDutyCycle(50)
		elif userInput == '0':
			led_pwm.ChangeDutyCycle(0)

except KeyboardInterrupt:
	print("fucked")
	led_pwm.stop()
	GPIO.cleanup()
	