import time
import board #type: ignore
import digitalio #type: ignore
import pwmio #type: ignore
from adafruit_motor import servo #type: ignore
import simplio #type: ignore
from digitalio import DigitalInOut,Direction,Pull #type: ignore
# set up my leds and button

greenled = digitalio.DigitalInOut(board.GP0)
redled = digitalio.DigitalInOut(board.GP1)
redled.direction = digitalio.Direction.OUTPUT
greenled.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP2)
button.pull = digitalio.Pull.DOWN
button.direction = digitalio.Direction.INPUT

pwm_servo = pwmio.PWMOut(board.GP3, duty_cycle=2**15, frequency=50)
my_servo = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)

print("on")
# same countdown with a blinking red light
while True:
    if (button.value == True): #If the button has been pushed:
        print("button")
        for i in range(10,0,-1):
            print(i)
            redled.value = True
            time.sleep(.5)
            redled.value = False
            time.sleep(.5)
            # when the countdown finishes, print liftoff and turn led on
        print("Liftoff!")
        my_servo.angle = 0
        greenled.value = True
        time.sleep(10)
        greenled.value = False