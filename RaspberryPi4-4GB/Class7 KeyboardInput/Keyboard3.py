import RPi.GPIO as GPIO
import time

servo_pin = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
servo_pwm=GPIO.PWM(servo_pin, 100)
servo_pwm.start(0)

servo_pwm_min = 3
servo_pwm_max = 12

try:
	while True:
		userInput = input("Enter a brightness percentage (q, w, e): ")
		if userInput == 'q':
			servo_pwm.ChangeDutyCycle(servo_pwm_min+((servo_pwm_max-servo_pwm_min)/90)*0)
		elif userInput == 'w':
			servo_pwm.ChangeDutyCycle(servo_pwm_min+((servo_pwm_max-servo_pwm_min)/90)*90)
		elif userInput == 'e':
			servo_pwm.ChangeDutyCycle(servo_pwm_min+((servo_pwm_max-servo_pwm_min)/90)*180)

except KeyboardInterrupt:
	print("fucked")
	servo_pwm.stop()
	GPIO.cleanup()
	