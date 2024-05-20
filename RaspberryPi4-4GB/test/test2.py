import RPi.GPIO as GPIO
import time
import threading

system_hault = False

out_pin = {"red":17, "green":27, "yellow":18, "servo":19}
GPIO.setmode(GPIO.BCM)
GPIO.setup(out_pin["red"], GPIO.OUT)
GPIO.setup(out_pin["green"], GPIO.OUT)
GPIO.setup(out_pin["yellow"], GPIO.OUT)
GPIO.setup(out_pin["servo"], GPIO.OUT)
yellow_pwm = GPIO.PWM(out_pin["yellow"], 100)
yellow_pwm.start(0)

servo_pwm = GPIO.PWM(out_pin["servo"], 50)
servo_pwm.start(0)

def green_led():
	while not system_hault:
		GPIO.output(out_pin["green"], GPIO.HIGH)
		time.sleep(0.6)
		GPIO.output(out_pin["green"], GPIO.LOW)
		time.sleep(0.6)

def mapper(value, in_min, in_max, out_min, out_max):
	return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def yellow_led():
	while not system_hault:
		for i in range(0, 1024, 1):
			yellow_pwm.ChangeDutyCycle(mapper(i, 0, 1024, 0, 100))
			time.sleep(0.001)
		for i in range(1024, 0, -1):
			yellow_pwm.ChangeDutyCycle(mapper(i, 0, 1024, 0, 100))
			time.sleep(0.001)
	yellow_pwm.stop()
	print("yellow haulted")

def servo():
	# while not system_hault:
	for i in range(0, 180, 1):
		servo_min = 2
		servo_max = 12.5
		servo_pwm.ChangeDutyCycle((servo_max-servo_min)/180 * i + servo_min)
		time.sleep(0.02)
	servo_pwm.stop()
	print("servo haulted")


green_thread = threading.Thread(target=green_led)
yellow_thread = threading.Thread(target=yellow_led)
servo_thread = threading.Thread(target=servo)

green_thread.start()
yellow_thread.start()
servo_thread.start()

try:
	while not system_hault:
		GPIO.output(out_pin["red"], GPIO.HIGH)
		time.sleep(0.3)
		GPIO.output(out_pin["red"], GPIO.LOW)
		time.sleep(0.3)

except KeyboardInterrupt:
	system_hault = True
	time.sleep(1)
	GPIO.cleanup()
	green_thread.join()
	yellow_thread.join()
	servo_thread.join()
	print("System Haulted")

GPIO.cleanup()
