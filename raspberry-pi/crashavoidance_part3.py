#type: ignore
import time #delay library
import board #board library
import adafruit_mpu6050 #accelerometer library
import busio
import digitalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio

displayio.release_displays()

led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT

sda = board.GP14 #SDA pin
scl = board.GP15 #SCL pin
i2c = busio.I2C(scl,sda) #I2C device declaration

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP2)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)


mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68) #accelerometer

while True: #if the z value is less than 7
    if (mpu.acceleration[2] < 7):
        print("on")
        led.value = True #turn the led on
    else:
        print("off")#if not
        led.value = False#turn the led off