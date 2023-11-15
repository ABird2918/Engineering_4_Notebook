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

with open("/data.csv", "a") as datalog:
    while True: #if the z value is less than 7
        runtime = time.monotonic()
        xacc = mpu.acceleration[0]
        yacc = mpu.acceleration[1]
        zacc = mpu.acceleration[2]
        if (zacc < 2):
            tilt = True
        else:
            tilt = False
        datalog.write(f"{runtime},{xacc},{yacc},{zacc},{tilt}\n")
        led.value = True
        time.sleep(.25)
        led.value = False
        time.sleep(.25)