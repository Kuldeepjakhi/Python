#!/usr/bin/python3
# upper() and lower() method example

answer = 'Yes'

print(answer.upper())
print(answer.lower())

print('Hello There!'.upper())

if answer.lower() == 'yes' or answer.upper() == 'YES':
	print("Playing Again")


if 'Hello'.upper().isupper():
	print('String is Upper')