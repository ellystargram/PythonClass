import spidev
import time
import RPi.GPIO as GPIO

spi=spidev.SpiDev()
spi.open(0,0)

spi.max_speed_hz=1350000

GPIO.setmode(GPIO.BCM)

led_pin = 17
GPIO.setup(led_pin, GPIO.OUT)

def analog_read(channel):
	r=spi.xfer2([1,(8+channel)<<4,0])
	adc_out=((r[1]&3)<<8)+r[2]
	return adc_out

while True:
	a = analog_read(7)
	print("ADC Value: "+str(a))
	if a >= 500:
		GPIO.output(led_pin, 1)
	else:
		GPIO.output(led_pin, 0)
	time.sleep(0.5)