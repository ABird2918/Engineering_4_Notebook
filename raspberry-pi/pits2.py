#type: ignore
import time
import digitalio
import board
import adafruit_lsm6dso32.LSM6DSO32

sensor = adafruit_lsm6dso32
#altitude = sensor.altitude
while True: 
# create the display group
    
    #print(f"{sensor.altitude}")  
    data = f"\n{round(sensor.gyro[0],3)}, {round(sensor.gyro[1],3)}, {round(sensor.gyro[2],3)}"
    print(data)