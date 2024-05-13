import RPi.GPIO as GPIO
import threading as th
import time

led_red_pin = 18
led_green_pin = 19
led_red_operate = True

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_red_pin, GPIO.OUT)
GPIO.setup(led_green_pin, GPIO.OUT)

led_red_pwm = GPIO.PWM(led_red_pin, 100)
led_green_pwm = GPIO.PWM(led_green_pin, 100)

led_red_pwm.start(0)
led_green_pwm.start(0)

def led_red_thread():
    while led_red_operate:
        one_way_time = 0.7/2
        for i in range(0, 101, 1):
            led_red_pwm.ChangeDutyCycle(i)
            time.sleep(one_way_time/100)
        for i in range(100, -1, -1):
            led_red_pwm.ChangeDutyCycle(i)
            time.sleep(one_way_time/100)

def led_green_thread():
    while True:
        one_way_time = 1.3/2
        for i in range(0, 101, 1):
            led_green_pwm.ChangeDutyCycle(i)
            time.sleep(one_way_time/100)
        for i in range(100, -1, -1):
            led_green_pwm.ChangeDutyCycle(i)
            time.sleep(one_way_time/100)

led_red_work = th.Thread(target=led_red_thread)
led_red_work.start()

try:
    while True:
        led_green_thread()
except KeyboardInterrupt:
    print("fucked")
    led_red_operate = False
    led_red_work.join()

led_red_pwm.stop()
led_green_pwm.stop()
GPIO.cleanup()
