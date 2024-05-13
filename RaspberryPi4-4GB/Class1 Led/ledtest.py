import RPi.GPIO as GPIO
import time

pwmPin =12
led1 = 23
led2 = 24
led1bool = False
led2bool = True
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(pwmPin, GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 1000)
pwm.start(0)

try:
    while True:
        for i in range(5):
            led1bool = not led1bool
            led2bool = not led2bool
            GPIO.output(led1, led1bool)
            GPIO.output(led2, led2bool)
            time.sleep(1)
            led1bool = not led1bool
            led2bool = not led2bool
            GPIO.output(led1, led1bool)
            GPIO.output(led2, led2bool)
            time.sleep(1)
        for i in range(10):
            pwm.ChangeDutyCycle(i*10)
            time.sleep(0.2)
        for i in range(9,-1,-1):
            pwm.ChangeDutyCycle(i*10)
            time.sleep(0.2)
    
except KeyboardInterrupt:
    print("done")
finally:
    pwm.stop()
    GPIO.cleanup()
#오등분의 신부 배경화면