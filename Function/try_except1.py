#!/usr/bin/python3
try:
	print('How many dog do you have ?')
	catNum = input()
	if int(catNum) >= 4 :
		print('That is a lot cats')
	else:
		print('That is not that many cats')
except ValueError:
	print('Please Enter Numeric value')