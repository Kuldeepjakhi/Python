#!/usr/bin/python3
import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    player1_choice = random.choice(choices)
    player2_choice = random.choice(choices)

    while True:
        print("Player 1 chose:", player1_choice)
        print("Player 2 chose:", player2_choice)

        if player1_choice == player2_choice:
            print("It's a tie! Let's play again.")
        elif (player1_choice == "rock" and player2_choice == "scissors") or \
             (player1_choice == "paper" and player2_choice == "rock") or \
             (player1_choice == "scissors" and player2_choice == "paper"):
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            break

play_game()