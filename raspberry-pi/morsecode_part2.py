#type: ignore
import time
import digitalio
import board

led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT

MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}

modifier = 0.25
dot_time = 1*modifier
dash_time = 3*modifier
between_taps = 1*modifier
between_letters = 3*modifier
between_words = 7*modifier

while True:
    message = input("Your Message: ").upper()
    tmessage = ""
    if "-q" in message
        break
    for letter in range(len(message)):
        tmessage = +- MORSE_CODE[message(letter)] + " "
        print(f"Translation:{tmessage}")
        time.sleep(1)
    for character in morse_message:
            if character = "."
                led = True
                time.sleep(.2)
                led = False
                time.sleep(.6)
            if character = "-"
                led = True
                time.sleep(.6)
                led = False
                time.sleep(.6)
            if character = " "
                time.sleep(1.4)


