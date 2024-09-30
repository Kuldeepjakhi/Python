#!/usr/bin/python3
import random
print('Hey what is your name ?')
name = input()

print('Hey', name, 'I am thinking Number between 1 to 20')
secretNum = random.randint(1, 20)

for guessTaken in range(1,7):
	print('Can you guess the Number:')
	guess = int(input())

	if guess < secretNum:
		print('Your Guess is too low')
	elif guess > secretNum:
		  print('Your Guess is too High')
	else: break

if guess == secretNum:
	print('Hey, ' + name + ' You Guessed my Number in ' + str(guessTaken) + ' times' )
else:
	print('Your Guessed wrong, The number I was thinking ' + str(secretNum))