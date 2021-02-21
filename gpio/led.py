import time

import RPi.GPIO as GPIO

# power: 5.3V

# whew using pins 4, 17, 18, 27
#   red 4 was lit a little after start, before running this progrem
#   it was not possible to lit all LEDs at once, some went off always
#   some dependencies between pins?

# using these values as in one of the exercises
# -> behaving the same, still can't lid all leds at once

# after putting each LED its own resitor, and not using just one
# resiston on GND wire, as it's instructed int the booklet exercise,
# litting all LEDS at once works
LEDS = {"red": 4, "blue": 18, "green": 23, "yellow": 24}


def blink_all():

    def blink(pin):
        delay_on=0.04
        delay_off=0.07
        GPIO.output(pin, True)
        time.sleep(delay_on)
        GPIO.output(pin, False)
        time.sleep(delay_off)

    try:
        while True:
            for pin in LEDS.values():
                blink(pin)
            for pin in reversed(list(LEDS.values())[1:-1]):
                blink(pin)
    
    finally:
        GPIO.cleanup()


def snake():
    try:
        while True:
            for pin in LEDS.values():
                GPIO.output(pin, True)
                time.sleep(0.1)


            for pin in reversed(list(LEDS.values())):
                GPIO.output(pin, False)
                time.sleep(0.1)
    finally:
        GPIO.cleanup()


def setup():
    GPIO.setmode(GPIO.BCM)
    for pin in LEDS.values():
        GPIO.setup(pin, GPIO.OUT, initial=0)


def main():
    setup()
    blink_all()
    #snake()


if __name__ == "__main__":
    main()
