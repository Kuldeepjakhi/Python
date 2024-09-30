#!/usr/bin/python3
sum = 0
counter = 0
while True:
  input_value = input('Enter a number: ')
  if input_value == 'done' or input_value == "Done": break
  value = float(input_value)
  sum = sum + value #keeps track of the total sum
  counter = counter + 1 #keeps the count of number of inputs entered
average = sum / counter
print('Average:', average)