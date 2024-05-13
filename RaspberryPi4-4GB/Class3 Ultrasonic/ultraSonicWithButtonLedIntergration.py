import RPi.GPIO as GPIO
import time

trigerPin =23
echoPin=24
pwmLedPin=4
led1Pin = 18
led2Pin = 25
buttonPin = 7
led1Bool = True
led2Bool = False
dutyRate = 0
pwmIncrease = True

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(pwmLedPin, GPIO.OUT)
GPIO.setup(led1Pin, GPIO.OUT)
GPIO.setup(led2Pin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
pwm = GPIO.PWM(pwmLedPin, 100)
pwm.start(0)

GPIO.output(trigerPin, GPIO.LOW)

try:
    while True:
        GPIO.output(trigerPin, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(trigerPin, GPIO.LOW)
        while not GPIO.input(echoPin):
            pulse_start = time.time()
        while GPIO.input(echoPin):
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        print("Distance: %.2f cm" % distance)
        if distance < 10:
            GPIO.output(led1Pin, led1Bool)
            GPIO.output(led2Pin, led2Bool)
            led1Bool = not led1Bool
            led2Bool = not led2Bool
        else:
            GPIO.output(led1Pin, GPIO.LOW)
            GPIO.output(led2Pin, GPIO.LOW)
            
        if GPIO.input(buttonPin):
            pwm.ChangeDutyCycle(dutyRate)
            if pwmIncrease:
                dutyRate += 10
                if dutyRate >= 100:
                    pwmIncrease = False
            else:
                dutyRate -= 10
                if dutyRate <= 0:
                    pwmIncrease = True
        else:
            pwm.ChangeDutyCycle(0)
        
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    print()
    print("done.")