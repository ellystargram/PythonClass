import RPi.GPIO as GPIO

switch1 = 7
switch2 = 8

led1 = 18
led2 = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(switch1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(switch1):
            GPIO.output(led1, True)
        else:
            GPIO.output(led1, False)
        if GPIO.input(switch2):
            GPIO.output(led2, True)
        else:
            GPIO.output(led2, False)
except KeyboardInterrupt:
    print("System Fucked")
    GPIO.cleanup()
