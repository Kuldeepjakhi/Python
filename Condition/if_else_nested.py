#!/usr/bin/python3

name = input("Please Enter the Name:")
age = input("Please Enter the Age:")
email = input("Please Enter the Email:")
password = input("Please Enter the password:")

if name == "":
	print("Name Cann't be Empty")

else:
	if age.isdigit() == False:
		print("Please Enter valid Age")
        exit()
	if "@" not in email:
	    print("Please Enter Valid Email Address")
	    exit()

	if len(password) <= 8:
		print("Please Enter password with more than 8 character")
		exit()

	else:
		print("You have successfully Login.")
