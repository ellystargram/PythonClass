import RPi.GPIO as GPIO

button_pin = 22
servo_pin = 19
button_count = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(servo_pin, GPIO.OUT)
servo_pwm = GPIO.PWM(servo_pin, 50)
servo_pwm.start(0)
servo_min = 2.5
servo_max = 12.5

def button_callback(channel):
	global button_count
	button_count += 1
	mode = button_count%3
	if mode == 0:
		print("180deg")
		servo_pwm.ChangeDutyCycle(servo_min+(servo_max-servo_min)/180*180)
	elif mode == 1:
		print("0deg")
		servo_pwm.ChangeDutyCycle(servo_min+(servo_max-servo_min)/180*0)
	else:
		print("90deg")
		servo_pwm.ChangeDutyCycle(servo_min+(servo_max-servo_min)/180*90)

	print("Button Pressed "+str(button_count)+" times")

GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=button_callback)
try:
	while True:
		pass
except KeyboardInterrupt:
	GPIO.cleanup()
	print("GPIO Cleaned Up")
