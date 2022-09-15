#!/usr/bin/env python3
from pynput import keyboard

num = 0
# The event listener will be running in this block
with keyboard.Events() as events:
    event = events.get()
    # for event in events:
    if event == keyboard.Key.esc:
        num += 1
        print(num)
    else:
        print("Received event {}".format(event))
