#!/usr/bin/python3
while True:
	user_input = input('Please Enter your Name:')
	if user_input == 'end':
		print(f'This is the end of loop')
		break

	print('Hi', user_input)
