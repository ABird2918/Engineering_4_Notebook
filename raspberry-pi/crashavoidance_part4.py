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
import adafruit_mpl3115a2

#make sure we are declaring the display for the whole time:
displayio.release_displays()
#setup leds
led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT

sda = board.GP4 #SDA pin
scl = board.GP5 #SCL pin
i2c = busio.I2C(scl,sda) #I2C device declaration
sensor = adafruit_mpl3115a2.MPL3115A2(i2c) #identify what sensor i'm talking about

#set up what values i can measure from the altimeter
pressure = sensor.pressure
altitude = sensor.altitude
temperature = sensor.temperature

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP2)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68) #accelerometer

while True: 
# create the display group

    splash = displayio.Group()
    #print('Pressure: {0:0.3f} pascals'.format(sensor.pressure))
    #print('Altitude: {0:0.3f} meters'.format(sensor.altitude))
    
    print(f"{sensor.altitude}")#prints the altitude in the format I want it to the terminal

    #print('Temperature: {0:0.3f} degrees Celsius'.format(sensor.temperature))
# add title block to display group
    title = "ANGULAR VELOCITY"
# the order of this command is (font, text, text color, and location)
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
    splash.append(text_area)    
    text_area.text = f"{title}\n{round(mpu.gyro[0],3)}, {round(mpu.gyro[1],3)}, {round(mpu.gyro[2],3)}\n{sensor.altitude-altitude}"
    #PRINT TO THE DISPLAY BOARD
    display.show(splash)
    print(round(mpu.gyro[0],3)) #print
    if (mpu.acceleration[2] < 7) and (sensor.altitude-altitude)<3: 
        #if the z value is less than 7 AND the altitude is less than 3 meters more than what it started as
        led.value = True #turn the led on
    else:
    #if not
        led.value = False#turn the led off