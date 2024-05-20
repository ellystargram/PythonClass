import RPi.GPIO as GPIO
import time
import math

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

seta = 0

try:
	while True:
		seta += math.pi/180
		if seta>=math.pi*2:
			seta-=math.pi*2

		new_red = int(math.sin(seta)*127+128)<<16
		new_green = int(math.sin(seta+2*math.pi/3)*127+128)<<8
		new_blue = int(math.sin(seta+4*math.pi/3)*127+128)
		
		set_colour(new_red+new_green+new_blue)

		time.sleep(0.01)

except KeyboardInterrupt:
	print("User Fucked")

red.stop()
green.stop()
blue.stop()
for i in pins:
	GPIO.output(pins[i], GPIO.HIGH)
GPIO.cleanup()
