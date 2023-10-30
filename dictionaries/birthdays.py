#!/usr/bin/env python3


birthdays = { 'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4', }

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday datebase updated.')


for v in birthdays.values():
    print(v) # prints all the values in the dictionary

for k in birthdays.keys():
    print(k) # prints all the keys in the dictionary

for i in birthdays.items():
    print(i) # prints all the items in the dictionary (both the key and value)

for k, v in birthdays.items():
    print('Key ' + v + ' Value ' + str(v)) # prints all the items in the dictionary (both the key and value)

birthdays.setdefault('Kevin', 'Feb 2') # adds the key value to the dictionary if the key isn't present already

picnicItems = { 'apples': 5, 'cups': 2 }
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
# I am bringing 2 cups.
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')
# I am bringing 0 eggs.
