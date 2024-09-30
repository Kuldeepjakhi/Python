#!/usr/bin/python3

dict1 = {'type' : 'fruit', 'name' : 'banana', 'taste' : 'sweet'}
dict2 = {'city' : 'Dehradun', 'state' : 'uttarakhand', 'country' : 'India'}

for x in dict1.values():
	print(x)

for a, b in dict2.items():
	print(a, b)

for y in dict2.items():
	print(y)