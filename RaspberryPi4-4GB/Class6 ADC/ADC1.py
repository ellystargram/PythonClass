import spidev
import time

spi=spidev.SpiDev()
spi.open(0,0)

spi.max_speed_hz=1350000

def analog_read(channel):
	r=spi.xfer2([1,(8+channel)<<4,0])
	adc_out=((r[1]&3)<<8)+r[2]
	return adc_outa

while True:
	a = analog_read(0)
	print("ADC Value: "+str(a))
	time.sleep(0.5)