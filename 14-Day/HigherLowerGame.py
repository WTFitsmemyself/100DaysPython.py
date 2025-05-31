from os import system, name
from telnetlib import GA
from Art import logo, vs
from random import randint
import GameData

GameContinue = True
Score = 0

def LuckyNumbers():
    NumberA = randint(0,49)
    NumberB = randint(0,49)
    if NumberA == NumberB:
        LuckyNumbers()
    return NumberA, NumberB

def ShowCompares(intCompareA, intCompareB):
    FullInfoA = GameData.data[intCompareA]
    FullInfoB = GameData.data[intCompareB]
    nameA = FullInfoA["name"]
    nameB = FullInfoB["name"]
    careerA = FullInfoA["description"]
    careerB = FullInfoB["description"]
    countryA = FullInfoA["country"]
    countryB = FullInfoB["country"]
    follower_countA = FullInfoA["follower_count"]
    follower_countB = FullInfoB["follower_count"]
    print(f"Compare A: {nameA}, {careerA}, from {countryA}.")
    print(vs)
    print(f"Against B: {nameB}, {careerB}, from {countryB}.")
    return follower_countA, follower_countB

def compareResult(FollowerA, FollowerB, UserChoice):
    if FollowerA > FollowerB and UserChoice == 'a':
        return True
    elif FollowerB > FollowerA and UserChoice == 'b':
        return True
    else:
        return False
     
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def Game():
    global Score
    global GameContinue
    while GameContinue:
        clear()
        print(logo)
        if Score > 0:
            print(f"You're right! Current Score: {Score}")
        NumberA, NumberB = LuckyNumbers()
        FollowerA1, FollowerB1 = ShowCompares(NumberA, NumberB)
        UserAnswer = input("Who has more followers? Type 'A' or 'B': ").lower()
        if compareResult(FollowerA1,FollowerB1,UserAnswer) == False:
            print(f"Sorry, that's wrong. Final Score: {Score}")
            GameContinue = False
        else:
            Score += 1
            print(f"You're right! Current score: {Score}.")
            Game()

Game()