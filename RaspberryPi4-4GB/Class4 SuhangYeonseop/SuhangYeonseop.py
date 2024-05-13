import RPi.GPIO as GPIO
import time

switch = 4
led1 = 17
led2 = 27
trigger = 23
echo = 24
led_pwm = 22

distance_output_unit = "cm"
timer = 0
led1_bool = True
led2_bool = False
led_mode = "blinking"
switch_before = False
switch_current = False
distance_timer = 0
debug = True
pwm_raising_direction = True
pwm_raising_timer=0
pwm_raising_enabled = False
duty_rate = 0                                                                                                                                                                                                                    

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(led_pwm, GPIO.OUT)

pwm_control = GPIO.PWM(led_pwm, 100)
pwm_control.start(0)


def measure_distance():
    GPIO.output(trigger, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigger, GPIO.LOW)
    while not GPIO.input(echo):
        start_time = time.time()
    while GPIO.input(echo):
        end_time = time.time()
    duration = end_time - start_time
    
    distance = duration * 17000
        
    return distance
    
    
try:
    while True:
        switch_current = GPIO.input(switch)
        if not switch_current and switch_before:
            if led_mode == "blinking":
                led_mode = "all_on"
            elif led_mode == "all_on":
                led_mode = "blinking"
            
        
        if led_mode == "blinking" and timer >=200:
            GPIO.output(led1, led1_bool)
            GPIO.output(led2, led2_bool)
            led1_bool = not led1_bool
            led2_bool = not led2_bool
            timer=0
        elif led_mode == "all_on":
            GPIO.output(led1, GPIO.HIGH)
            GPIO.output(led2, GPIO.HIGH)
            timer=0
            
        if distance_timer >=500:
            distance_timer=0
            distance = measure_distance()
            if debug:
                print("Distance: %.2f %s" % (distance, distance_output_unit))
            if distance == -1:
                print("Distance is out of range.")
            elif distance <= 10:
                pwm_raising_enabled = True
            else:
                pwm_raising_timer=0
                pwm_raising_enabled = False
                pwm_control.ChangeDutyCycle(0)
                
        if pwm_raising_timer >= 100 and pwm_raising_enabled:
            pwm_raising_timer=0
            if pwm_raising_direction:
                duty_rate+=10
                pwm_control.ChangeDutyCycle(duty_rate)
                if duty_rate >= 100:
                    pwm_raising_direction = False
            else:
                duty_rate-=10
                pwm_control.ChangeDutyCycle(duty_rate)
                if duty_rate <= 0:
                    pwm_raising_direction = True
                
                

            
        time.sleep(0.001)
        timer+=1
        distance_timer+=1
        if pwm_raising_enabled:
            pwm_raising_timer+=1
        switch_before = switch_current
        
except KeyboardInterrupt:
    print("done.")

GPIO.cleanup()
