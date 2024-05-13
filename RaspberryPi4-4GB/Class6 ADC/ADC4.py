import spidev
import time
import RPi.GPIO as GPIO

spi=spidev.SpiDev()
spi.open(0,0)

spi.max_speed_hz=1350000

GPIO.setmode(GPIO.BCM)

led_pin = 17
GPIO.setup(led_pin, GPIO.OUT)
pwm_pin = 18
GPIO.setup(pwm_pin, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin, 100)
pwm.start(0)

def analog_read(channel):
	r=spi.xfer2([1,(8+channel)<<4,0])
	adc_out=((r[1]&3)<<8)+r[2]
	return adc_out

while True:
	a = analog_read(7)
	print("ADC Value: "+str(a))
	pwm.ChangeDutyCycle(a/10.24)
	if a != 0:
		GPIO.output(led_pin, 1)
	else:
		GPIO.output(led_pin, 0)
	time.sleep(0.1)