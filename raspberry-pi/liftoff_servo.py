import time
import board #type: ignore
import digitalio #type: ignore
import pwmio #type: ignore
from adafruit_motor import servo #type: ignore
from digitalio import DigitalInOut,Direction,Pull #type: ignore
# set up my leds and button

greenled = digitalio.DigitalInOut(board.GP0)
redled = digitalio.DigitalInOut(board.GP1)
redled.direction = digitalio.Direction.OUTPUT
greenled.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP2)
button.pull = digitalio.Pull.DOWN
button.direction = digitalio.Direction.INPUT
#setup my servo
pwm_servo = pwmio.PWMOut(board.GP3, duty_cycle=2**15, frequency=50)
my_servo = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)

my_servo.angle = 0
#have the servo start at 0 degrees

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
        greenled.value = True
        greenled.value = False
        #when the angle of the servo is in the range, move it 180 degrees
        for angle in range(0, 185, 180):
            my_servo.angle = angle
            #print the angle to make sure everything is working smoothly
            print(angle)
        time.sleep(10)