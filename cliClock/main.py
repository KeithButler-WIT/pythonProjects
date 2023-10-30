#!/usr/bin/env python3

import pyfiglet

from time import strftime


def main():
    while True:
        digital_clock()


def digital_clock():
    # tick = strftime("%H:%M:%S %p")
    tick = strftime("%H:%M")
    time_to_ascii(tick)


def time_to_ascii(time):
    result = pyfiglet.figlet_format(time, font="doh")
    print(result)


if __name__ == "__main__":
    main()
