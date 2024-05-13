import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
led=18
switch=7
GPIO.setup(led, GPIO.OUT)
GPIO.setup(switch, GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(switch):
        GPIO.output(led, True)
    else:
        GPIO.output(led, False)
