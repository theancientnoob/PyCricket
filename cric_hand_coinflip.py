
import random
from time import sleep

coinflip_win_status_bat = False
coinflip_win_status_bowl = False

coinflip_choice = ["heads","tails"]
bat_bowl_random = ["bat","bowl"]

while True:
    coinflip = input("Heads or Tails?")
    
    if coinflip == "heads":
        print("You have chosen Heads.")
        break

    elif coinflip == "tails":
        print("You have chosen tails")
        break

    else:
        print("try again.")


comp_coinflip = random.choice(coinflip_choice)


sleep(2)


if comp_coinflip == "heads" and coinflip == "heads":
    print("Yay! The coin turns to Heads! You win the Coin Flip!")

    while True:
        bat_bowl_choice = input("Do you wish to bat or bowl?")
        if bat_bowl_choice == "bat":
            coinflip_win_status_bat = True
            break

        elif bat_bowl_choice == "bowl":
            coinflip_win_status_bowl = True
            break

        else:
            print("invalid input. Try again.")

elif comp_coinflip == "heads" and coinflip == "tails":
    print("uh oh! The coin turns to Heads! You lose the Coin Flip!")

    while True:
        comp_choice_bat_ball = random.choice(bat_bowl_random)
        if comp_choice_bat_ball == "bat":
            print("The computer chose batting, so you will be bowling.")
            break

        elif comp_choice_bat_ball == "bowl":
            print("The computer chose bowling. So you will be batting.")
            break

        else:
            print("Invalid input, try again.")

elif comp_coinflip == "tails" and coinflip == "tails":
    print("Yay! The coin turns to Tails! You win the Coin Flip!")

    while True:
        bat_bowl_choice = input("Do you wish to bat or bowl?")
        if bat_bowl_choice == "bat":
            coinflip_win_status_bat = True
            break

        elif bat_bowl_choice == "bowl":
            coinflip_win_status_bowl = True
            break

        else:
            print("invalid input. Try again.")

elif comp_coinflip == "tails" and coinflip == "heads":
    print("uh oh! The coin turns to Tails! You lose the Coin Flip!")

    while True:
        comp_choice_bat_ball = random.choice(bat_bowl_random)
        if comp_choice_bat_ball == "bat":
            print("The computer chose batting, so you will be bowling.")
            break

        elif comp_choice_bat_ball == "bowl":
            print("The computer chose bowling. So you will be batting.")
            break

        else:
            print("Invalid input, try again.")


 
sleep(2)


if coinflip_win_status_bat == True: 
    def coinflip_win_status_bat_act():
        
        score = 0


        '1' == 1
        '2' == 2
        '3' == 3
        '4' == 4
        '5' == 5
        '6' == 6



        keywords = ['1','2','3','4','5','6','score']

        comp_roll = ['1','2','3','4','5','6']


        while True:
            user_roll = (input("Its your turn! Type a number from 1 to 6!"))

            if type(user_roll) == str:

                comp_choice = random.choice(comp_roll)

                if user_roll in keywords:

                    if user_roll in keywords and user_roll != "score":
                        for char in user_roll:
                            if char.isdigit():
                                score += int(char)
                                print("You typed",user_roll)

                    if user_roll == "score":
                        print("Your score is:",score)

                    if user_roll == comp_choice:
                        sleep(2)
                        print("Uh Oh! You and the computer rolled a", user_roll)
                        sleep(2)
                        print("YOU")
                        sleep(1)
                        print("ARE")
                        sleep(1)
                        print("OUT!!")
                        sleep(1)
                        print("Your total score was:",score)
                        break

                else:
                    print("Invalid. Try again.")
                    
            else:
                print("invalid. numbers are only alllowed.")
    coinflip_win_status_bat_act()

if coinflip_win_status_bowl == True:
    def coinflip_win_status_bowl_act():

        keywords = ['1','2','3','4','5','6','score']

        comp_roll = ['1','2','3','4','5','6']

        score = 0


        print("The computer will be batting. Your objective is to match the computer's roll to knock it out.")

        while True:
            user_roll_bowl = input("Type a number from 1 to 6 ")

            if  type(user_roll_bowl) == str:
                if user_roll_bowl in keywords:
                    comp_choice_bat = random.choice(comp_roll)

                    if comp_choice_bat != user_roll_bowl and user_roll_bowl != "score":
                        for char in comp_choice_bat:
                                if char.isdigit():
                                    score += int(char)
                        print("You typed",user_roll_bowl,"and the computer rolled",comp_choice_bat)

                    elif user_roll_bowl == "score":
                        print("The score is",score)

                    elif comp_choice_bat == user_roll_bowl:
                        sleep(2)
                        print("Yay! You and the computer rolled a", user_roll_bowl)
                        sleep(2)
                        print("YOU")
                        sleep(1)
                        print("KNOCKED")
                        sleep(1)
                        print("THE COMPUTER")
                        sleep(1)
                        print("OUT!!")
                        sleep(1)
                        print("The total score was:",score)
                        break

                        



                else:
                    print("Invalid. Try again.")
                

            else:
                print("invalid. Try again.")

    coinflip_win_status_bowl_act()
