#!/usr/bin/python3
# check key exist and compare two dictionaries value.

thisdict1 = {

	"name": "Daksh", 
	"age": "3", 
	"country": "India"
	}

thisdict2 = {

	"country": "India",
	"name": "Daksh", 
	"age": "3" 
	
	}

if 'school' not in thisdict1:
	print("School key is not there in thisdict1 ")
	
if thisdict1 == thisdict2:
	print("Value of thisdict1 and thisdict2 are same")
else:
    print("Value of thisdict1 and thisdict2 are not identical")
