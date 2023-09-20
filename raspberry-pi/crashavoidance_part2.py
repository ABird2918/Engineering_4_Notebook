#type: ignore
import time #delay library
import board #board library
import adafruit_mpu6050 #accelerometer library
import busio
import digitalio

led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT

sda = board.GP14 #SDA pin
scl = board.GP15 #SCL pin
i2c = busio.I2C(scl,sda) #I2C device declaration

mpu = adafruit_mpu6050.MPU6050(i2c) #accelerometer

while True: #if the z value is less than 7
    if (mpu.acceleration[2] < 7):
        print("on")
        led.value = True #turn the led on
    else:
        print("off")#if not
        led.value = False#turn the led off