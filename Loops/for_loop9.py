#!/usr/bin/python3
num = int(input("Enter the Number: "))
flag = 0
if num < 2:
	print("Number is not prime number")
else:
	for x in range(2,num):
		if (num%i) == 0:
			flag = 1
			break
	if flag == 1:
  print('Not Prime')
else:
  print("Prime")