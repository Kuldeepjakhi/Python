#!/usr/bin/python3
ind_list = [133,15,36,16,18,35,22,36,89,93,78,56]
index = 0
while index < len(ind_list):
	num = ind_list[index]
	if num%2 == 0:
		print(num, "Is Even Number")
#		break
	else:
		print(num, "is Odd Number")
	index += 1

