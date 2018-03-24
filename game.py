#!/bin/python
import random

rock = 'камень'
scissors = 'ножницы'
paper = "бумага"
x = "да"
while x == "да" or x == "y":

    player_input = input("что загадываешь? Камень ножницы или бумагу? or [r/p/s] ")

    print('Rock, paper, scissors!')

    ran = random.choice([rock,paper,scissors])
    print(ran)


    if player_input == rock or player_input == "r": 
        if ran == rock:
            print("Draw!")
        elif ran == scissors:
            print("I've lost!")
        elif ran == paper:
            print("You've lost!")
    if player_input == scissors or player_input == "s": 
        if ran == rock:
            print("You've lost!")
        elif ran == scissors:
            print("Draw!")
        elif ran == paper:
            print("I've lost!")
    if player_input == paper or player_input == "p":
        if ran == rock:
            print("I've lost!")
        elif ran == scissors:
            print("You've lost!")
        elif ran == paper:
            print("Draw!")
    x = input("Ещё раз? [да/нет] or [y/n] ") 