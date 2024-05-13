import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
for i in range(1,20):
    GPIO.output(5, True)
    GPIO.output(6, False)
    time.sleep(2)
    GPIO.output(5, False)
    GPIO.output(6, True)
    time.sleep(2)