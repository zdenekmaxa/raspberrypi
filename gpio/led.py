"""
Blinkind LEDs via GPIO.

Raspberry Pi power: 5.3V

According to Conrad experiments booklet.

Using 4, 17, 18, 27 GPIO pins. Also 4, 18, 23, 24.

Connecting just one resistor on GND branch doesn't properly work:
    not possible to lit all LEDs at once, some turned off when setting all
    pins True (blink_all() function). Each LED needs to have resistor on the
    + (set pin) branch - turning all LEDs at once is possible.

Connection:
    black: common GND pin
    red, blue, green, yellow to corresponding LEDs
    red: pin 4
    blue: pin 18
    green: pin 23
    yellow: pin 24

LED: 
    anode: + (longer pin)
    cathode: - (shorter pin)
    + ---|>|--- -

"""

import time

import RPi.GPIO as GPIO


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

