#!/usr/bin/python3
# upper() and lower() method example

myvar1 = 'Hello'
myvar2 = '123456'
myvar3 = 'Hello123'
myvar4 = 'Hello There'
myvar5 = 'hey dude!'


if myvar1.isalpha():
	print(f'In \'{myvar1}\' string all are alphabets')

if myvar2.isdecimal():
	print(f"In \'{myvar2}\' all are numbers")

if myvar3.isalnum():
	print(f"In \'{myvar3}\' all are Alpha numeric")

print()
