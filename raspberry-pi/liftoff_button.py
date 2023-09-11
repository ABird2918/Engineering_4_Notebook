import time
import board #type: ignore
import digitalio #type: ignore
# set up my leds and button
greenled = digitalio.DigitalInOut(board.GP0)
redled = digitalio.DigitalInOut(board.GP1)
redled.direction = digitalio.Direction.OUTPUT
greenled.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP2)
button.pull = digitalio.Pull.DOWN
button.direction = digitalio.Direction.INPUT
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
        time.sleep(10)
        greenled.value = False