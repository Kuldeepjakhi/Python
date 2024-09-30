#!/usr/bin/python3
fact = 1
num = int(input('Please Enter the number for factorial:'))
for x in range(fact,num + 1):
	fact = fact * x
print(fact)