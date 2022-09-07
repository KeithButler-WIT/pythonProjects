#!/usr/bin/env python3

import json
from pynput.keyboard import Key, Listener, Events
from os.path import exists as file_exists

counter_file = "counter.txt"


def main():
    load()
    mainMenu()


def mainMenu():
    while True:
        print(
            """
            Press a button

            s: save to text file
            l: list all counters
            c: count
            n: add new counter
            q: quit program
            """
        )
        run(input("enter a key: "))


def run(key):
    print(key)
    match key:
        case "s":
            return save()
        case "l":
            return listCounters()
        case "c":
            return counterRun()
        case "n":
            return quit()
        case "d":
            return deleteCounter()
        case "q":
            return quit()
        case default:
            print("Invalid key input")


# TODO: add the option to pick counter from name
def counterPick():
    while True:
        listCounters()
        try:
            counterNum = int(input("enter a key: "))
            return counterNum
        except:
            print("No counter matches that number")


# NOTE kinda works but double counts because it does both press and release
def counterRun():
    counterNum = counterPick()
    print("Now counting")
    # The event listener will be running in this block
    with Events() as events:
        for event in events:
            if event.key == Key.enter:
                counter_dict[counterNum]["number"] += 1
                print(counter_dict[counterNum]["number"])
            elif event.key == Key.backspace:
                counter_dict[counterNum]["number"] -= 1
                print(counter_dict[counterNum]["number"])
            elif event.key == Key.esc:
                return


# def counterRun():
#     listCounters()
#     counterNum = counterPick()
#     print("Now counting")
#     # The event listener will be running in this block
#     with Events() as events:
#         while True:
#             event = events.get()
#             if event == Key.enter:
#                 counter_dict[counterNum]["number"] += 1
#                 print(counter_dict[counterNum]["number"])
#             elif event == Key.backspace:
#                 counter_dict[counterNum]["number"] += 1
#                 print(counter_dict[counterNum]["number"])
#             elif event == Key.esc:
#                 break


# Test disctionary variable
counter_dict = {
    0: {"name": "actual name", "number": 10},
    1: {"name": "actual name 2", "number": 5},
}


def deleteCounter():
    print("Pick a counter to delete")
    counterNum = counterPick()
    del counter_dict[counterNum]


def save():
    json.dump(counter_dict, open(counter_file, "w"), indent=4)
    print("Counter dictionary saved")


def load():
    if file_exists(counter_file):
        counter_dict = json.load(open(counter_file))
    else:
        with open(counter_file, "w"):
            print("File created")


def listCounters():
    print(json.dumps(counter_dict, indent=4))
    # print(counter_dict.values())


## CODE LAYOUT ##
# if enter pressed:
#   counter++

#
## dictionary layout ##
# counter_dict = {
#     "counter1": {"name": "actual name", "number": 10},
#     "counter2": {"name": "actual name 2", "number": 5},
# }

if __name__ == "__main__":
    main()
