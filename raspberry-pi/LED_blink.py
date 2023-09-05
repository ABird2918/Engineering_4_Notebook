# type: ignore
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value(True)
    time.sleep(1)
    led.value(False)
    time.sleep(1)