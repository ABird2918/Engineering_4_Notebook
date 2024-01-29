#type: ignore
import time
import digitalio
import board
from adafruit_lsm6ds.lsm6dso32 import LSM6DSO32
import busio

sda = board.GP4 #SDA pin
scl = board.GP5 #SCL pin
i2c = busio.I2C(scl,sda) #I2C device declaration
sensor = LSM6DSO32(i2c)


#altitude = sensor.altitude
while True: 
# create the display group
    
    #print(f"{sensor.altitude}")  
    data = f"\n{round(sensor.acceleration[0],3)}, {round(sensor.acceleration[1],3)}, {round(sensor.acceleration[2],3)}"
    print(data)
    time.sleep(2)