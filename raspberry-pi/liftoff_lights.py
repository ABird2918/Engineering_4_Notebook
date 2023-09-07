import time
import board #type: ignore
import digitalio #type: ignore

greenled = digitalio.DigitalInOut(board.GP0)
redled = digitalio.DigitalInOut(board.GP1)
redled.direction = digitalio.Direction.OUTPUT
greenled.direction = digitalio.Direction.OUTPUT

for i in range(10,0,-1):
    print(i)
    redled.value = True
    time.sleep(.5)
    redled.value = False
    time.sleep(.5)


print("Liftoff!")
greenled.value = True
time.sleep(10)