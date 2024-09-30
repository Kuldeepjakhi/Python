#!/usr/bin/python3

name = 'Daksh'
print(f"My Name is {name}...")


a = 10
b = 15

print(f"The multplication of {a} and {b} is: {a*b}")


#Float precision in the f-String Method
num = 3.14159
print(f"The valueof pi is: {num:{1}.{5}}")


# Formatting string using center() method


example_string = "GeeksForGeeks!"
width = 30

centered_string = example_string.center(width)

print(centered_string)