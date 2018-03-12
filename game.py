#!/bin/python
import random

rock = 'камень'
scissors = 'ножницы'
paper = "бумага"
x = "да"
while x == "да":

    name = input("что загадываешь? Камень ножницы или бумагу? ")

    print('Rock, paper, scissors!')

    ran = random.choice([rock,paper,scissors])
    print(ran)


    if name == rock: 
        if ran == rock:
            print("Draw!")
        elif ran == scissors:
            print("I've lost!")
        elif ran == paper:
            print("You've lost!")
    if name == scissors: 
        if ran == rock:
            print("You've lost!")
        elif ran == scissors:
            print("Draw!")
        elif ran == paper:
            print("I've lost!")
    if name == paper:
        if ran == rock:
            print("I've lost!")
        elif ran == scissors:
            print("You've lost!")
        elif ran == paper:
            print("Draw!")
    x = input("Ещё раз? да/нет ")