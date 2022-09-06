#!/usr/bin/env python3


def main():
    while True:
        print(
            """
            Press a button

            s: save
            l: load
            n: new counter
            q: quit
            """
        )
        run(input("enter a key: "))


def run(key):
    print(key)
    match key:
        case "s":
            return save()
        case "l":
            return list()
        case "n":
            return quit()
        case "q":
            return quit()
        case default:
            print("Invalid key input")


counter_dict = {
    "counter1": {"name": "actual name", "number": 10},
    "counter2": {"name": "actual name 2", "number": 5},
}


def save():
    d = counter_dict
    with open("counter.txt", "w") as f:
        f.write(repr(d))


def list():
    pass


## CODE LAYOUT ##
# def load():
# if file.txt exists:
#   with open("file.txt", "r") as f
#   for line in f:
#       name = f.readline()
#       number = f.readline()
#       if line == None
#           f.close()
#           pass
# else create file.txt


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
