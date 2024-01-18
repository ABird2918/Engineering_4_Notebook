#type: ignore
import time
import digitalio
import board
import lsm6dso32

sensor = lsm6dso32(i2c)
sda = board.GP4 #SDA pin
scl = board.GP5 #SCL pin
i2c = busio.I2C(scl,sda) #I2C device declaration
#altitude = sensor.altitude
while True: 
# create the display group
    
    #print(f"{sensor.altitude}")  
    data = f"\n{round(sensor.gyro[0],3)}, {round(sensor.gyro[1],3)}, {round(sensor.gyro[2],3)}"
    print(data)