import random
import time

def easy():
    ran_num = random.randrange(1,11)

    while True:
        player_guess = int(input("Enter a number from 1 to 10:"))
        if player_guess < ran_num :
            print("It's too low")
        if player_guess > ran_num:
            print("it's too high")
        if player_guess == ran_num:
            print("You are correct.")
            break

def median():
    ran_num = random.randrange(1,101)

    while True:
        player_guess = int(input("Enter a number from 1 to 100:"))
        if player_guess < ran_num :
            print("It's too low")
        if player_guess > ran_num:
            print("it's too high")
        if player_guess == ran_num:
            print("You are correct.")
            break


def hard():
    ran_num = random.randrange(1, 1001)

    while True:
        player_guess = int(input("Enter a number from 1 to 1000:"))
        if player_guess < ran_num:
            print("It's too low")
        if player_guess > ran_num:
            print("it's too high")
        if player_guess == ran_num:
            print("You are correct.")
            break

def main():
    modehard2 = 'y'

    print("Welcome to the game. Here, you will guess numbers.")
    while modehard2 == 'y':
        print("Which mode do you want to play?")
        print("1.easy 2.median 3.hard 4.quit")
        modehard1=int(input("Choose a mode:"))
        if modehard1 != 4:
            time.sleep(1)
            print("Now the game starts.")
            if modehard1 == 1:
                easy()
            elif modehard1 == 2:
                median()
            elif modehard1 == 3:
                hard()
        else:
            print("The end.")

        print("Do you want to replay the game? ")
        print("y(yes) n(no)")
        modehard2 = raw_input("Enter your choice:")

main()

