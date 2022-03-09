#!/bin/python
import random

rock = "rock"
scissors = "scissors"
paper = "paper"
x = "yes"
while x == "yes" or x == "y":

    player_input = input("Pick one:[rock,paper,scissors] or [r/p/s] ")

    print("Rock, paper, scissors!")

    ran = random.choice([rock,paper,scissors])
    print("I chose " + ran + " and you chose " + player_input + ".")

    if player_input == "qwerty":
        print("You won, cheater! >:-( ")
    
    if player_input == rock or player_input == "r": 
        if ran == rock:
            print("Draw!")
        elif ran == scissors:
            print("I lost!")
        elif ran == paper:
            print("You lost!")
    if player_input == scissors or player_input == "s": 
        if ran == rock:
            print("You lost!")
        elif ran == scissors:
            print("Draw!")
        elif ran == paper:
            print("I lost!")
    if player_input == paper or player_input == "p":
        if ran == rock:
            print("I lost!")
        elif ran == scissors:
            print("You lost!")
        elif ran == paper:
            print("Draw!")
    x = input("Wanna play again? [yes/no] or [y/n] ") 