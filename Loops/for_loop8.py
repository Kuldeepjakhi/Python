#!/usr/bin/python3
l_range = int(input("Enter Lower Range to find prime: "))
u_range = int(input("Enter Upper Range to find prime: "))
print("Prime numbers between", l_range, "and", u_range, "are:")
for num in range(l_range, u_range + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, end=",")