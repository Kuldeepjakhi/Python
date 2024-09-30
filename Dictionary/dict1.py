#!/usr/bin/python3
cardict = {
	"brand": "Ford",
	"Model": "Mustang",
	"Year": 2024
}

print(cardict)      # Print complete Dictionary
print(cardict["brand"])   # Print specific key value

print(cardict.keys())  # Print only keys
print(cardict.values()) # Print only Values.
print(cardict.items()) # print both keys and values.

print("I Like " + cardict["brand"] + " " + cardict["Model"])