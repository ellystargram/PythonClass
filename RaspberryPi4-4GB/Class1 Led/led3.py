import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 100)
pwm.start(0)

while True:
    for i in range(0,101,1):
        pwm.ChangeDutyCycle(i)
        print(i)
        time.sleep(0.01)
    for i in range(100,-1,-1):
        pwm.ChangeDutyCycle(i)
        print(i)
        time.sleep(0.01)
