#!/usr/bin/python3
def div42by(dividedBy):
	try:
		return 42 / dividedBy
	except ZeroDivisionError:
		print('Error: You tried to divided by 0')
	
print(div42by(2))
print(div42by(3))
print(div42by(4))
print(div42by(0))
print(div42by(6))