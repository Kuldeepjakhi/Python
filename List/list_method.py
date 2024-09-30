#!/usr/bin/python3

spam = ['hey', 'Hi', 'howdy']
print(spam.index('hey'))  # index is method name

pet = ['cat','dog','rabbit','horse']
print(pet)

pet.append('elephant') # Append new item in the list.
print(pet)

pet.insert(3, 'cow') # Insert New item in 3rd index of list.
print(pet)

pet.remove('rabbit') # Remove Item in the list. If item is not exist it will give error msg.
print(pet)

del pet[3] # Delete 3rd index in list.
print(pet)

num = [3, 5, -3, 0, 13, 9, -8, 27, 45, 87, 46]
num.sort()  # Sort the items in list
print(num)

pet.sort(reverse=True) # Reverse Sorting
print(pet)

alpha = ['Alice', 'Robin', 'adam', 'Bob', 'Zack', 'sam']

alpha.sort() # This will sort uppercase first and then lowercase.
print(alpha)

alpha.sort(key=str.lower) # It will sort letters.
print(alpha)

"""
output
0
['cat', 'dog', 'rabbit', 'horse']
['cat', 'dog', 'rabbit', 'horse', 'elephant']
['cat', 'dog', 'rabbit', 'cow', 'horse', 'elephant']
['cat', 'dog', 'cow', 'horse', 'elephant']
['cat', 'dog', 'cow', 'elephant']
[-8, -3, 0, 3, 5, 9, 13, 27, 45, 46, 87]
['elephant', 'dog', 'cow', 'cat']
['Alice', 'Bob', 'Robin', 'Zack', 'adam', 'sam']
['adam', 'Alice', 'Bob', 'Robin', 'sam', 'Zack']

"""

