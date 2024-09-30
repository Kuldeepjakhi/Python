#!/usr/bin/python3
while True:
	user_input = input('Please enter number:')
	if user_input == "q" or user_input == "Q":
		print("Break Loop")
		break
	number=int(user_input)
	if number%2 == 0:
		print(number, "square is:",number*number)
		continue
	print(number, "is odd number")