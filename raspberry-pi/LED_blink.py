
import time
import board # type: ignore
import digitalio # type: ignore

led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT

redled = digitalio.DigitalInOut(board.GP1)
redled.direction = digitalio.Direction.OUTPUT

while True:
    redled.value = False
    led.value = True
    time.sleep(1)
    led.value = False
    redled.value = True
    time.sleep(1)