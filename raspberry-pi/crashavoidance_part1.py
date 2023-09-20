#type: ignore
import adafruit_mpu6050
import busio
import board
import time
import digitalio

#set up pins to my accelerometer
sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)

#set the mpu value = to the input from the accelerometer
mpu = adafruit_mpu6050.MPU6050(i2c)

while True: # constantly print the accelerometer value
    print(mpu.acceleration)
    time.sleep(.5) #twice per second