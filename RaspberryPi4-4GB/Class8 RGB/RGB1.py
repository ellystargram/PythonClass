import RPi.GPIO as GPIO
import time

colours = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0xFF00FF, 0x00FFFF, 0xFFFFFF]
pins={"red":16, "green":20, "blue":21}

GPIO.setmode(GPIO.BCM)
for i in pins:
	GPIO.setup(pins[i], GPIO.OUT)
	GPIO.output(pins[i], GPIO.HIGH)

red = GPIO.PWM(pins["red"], 2000)
green = GPIO.PWM(pins["green"], 2000)
blue = GPIO.PWM(pins["blue"], 2000)

red.start(0)
green.start(0)
blue.start(0)

def map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def set_colour(colour):
	red.ChangeDutyCycle(map((colour & 0xFF0000) >> 16, 0, 255, 0, 100))
	green.ChangeDutyCycle(map((colour & 0x00FF00) >> 8, 0, 255, 0, 100))
	blue.ChangeDutyCycle(map(colour & 0x0000FF, 0, 255, 0, 100))

try:
	while True:
		for colour in colours:
			set_colour(colour)
			time.sleep(0.5)
except KeyboardInterrupt:
	print("User Fucked")

red.stop()
green.stop()
blue.stop()
for i in pins:
	GPIO.output(pins[i], GPIO.HIGH)
GPIO.cleanup()
