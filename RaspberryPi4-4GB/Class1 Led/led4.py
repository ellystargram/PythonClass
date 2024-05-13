import RPi.GPIO as GPIO
import time

led=12
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
# pwm = GPIO.PWM(led, 100)
# pwm.start(0)

try:
    pwm=GPIO.PWM(led, 100)
    pwm.start(0)
    while True:
        for i in range(10):
            pwm.ChangeDutyCycle(i*10)
            print(i)
            time.sleep(1)
except KeyboardInterrupt:
    print("끝")
finally:
    pwm.stop()
    GPIO.cleanup()
    #이세계아이돌 배경화면