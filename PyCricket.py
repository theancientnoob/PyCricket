
import random
from time import sleep

while True:
    main_choice =  input("Do you want to play PyCricket? {y/n}")

    if main_choice == "y":
        def cric_hand_game():

            score_bat = 0
            score_comp = 0

            user_batting_done = False
            user_bowling_done = False

            coinflip_win_status_bat = False
            coinflip_win_status_bowl = False

            coinflip_choice = ["heads","tails"]
            bat_bowl_random = ["bat","bowl"]

            while True:
                coinflip = input("heads or tails?")
                
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
                        coinflip_win_status_bowl = True
                        break

                    elif comp_choice_bat_ball == "bowl":
                        print("The computer chose bowling. So you will be batting.")
                        coinflip_win_status_bat = True

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
                        coinflip_win_status_bowl= True
                        break

                    elif comp_choice_bat_ball == "bowl":
                        print("The computer chose bowling. So you will be batting.")
                        coinflip_win_status_bat = True
                        break

                    else:
                        print("Invalid input, try again.")


            
            sleep(2)


            if coinflip_win_status_bat == True: 
                user_batting_done = True
                def coinflip_win_status_bat_act():
                    
                    global user_score
                    user_score = 0


                    '1' == 1
                    '2' == 2
                    '3' == 3
                    '4' == 4
                    '5' == 5
                    '6' == 6



                    keywords = ['1','2','3','4','5','6','score']

                    comp_roll = ['1','2','3','4','5','6']

                    print("The computer will be bowling. Your objective is to keep scoring without typing a number that would match the computer's roll.")


                    while True:
                        user_roll = (input("Its your turn! Type a number from 1 to 6!"))

                        if type(user_roll) == str:

                            comp_choice = random.choice(comp_roll)

                            if user_roll in keywords:

                                if user_roll in keywords and user_roll != "score" and user_roll != comp_choice:
                                    for char in user_roll:
                                        if char.isdigit():
                                            user_score += int(char)
                                            print("You typed",user_roll)

                                if user_roll == "score":
                                    print("Your score is:",user_score)

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
                                    print("Your total score was:",user_score)
                                

                                    break

                            else:
                                print("Invalid. Try again.")
                                
                        else:
                            print("invalid. numbers are only alllowed.")
                coinflip_win_status_bat_act()
                score_bat = user_score

            if coinflip_win_status_bowl == True:
                user_bowling_done = True
                def coinflip_win_status_bowl_act():

                    keywords = ['1','2','3','4','5','6','score']

                    comp_roll = ['1','2','3','4','5','6']

                    global comp_score
                    comp_score = 0
                    


                    print("The computer will be batting. Your objective is to match the computer's roll to knock it out.")

                    while True:
                        user_roll_bowl = input("Type a number from 1 to 6 ")

                        if  type(user_roll_bowl) == str:
                            if user_roll_bowl in keywords:
                                comp_choice_bat = random.choice(comp_roll)

                                if comp_choice_bat != user_roll_bowl and user_roll_bowl != "score":
                                    for char in comp_choice_bat:
                                            if char.isdigit():
                                                comp_score += int(char)
                                    print("You typed",user_roll_bowl,"and the computer rolled",comp_choice_bat)

                                elif user_roll_bowl == "score":
                                    print("The score is",comp_score)

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
                                    print("The total score was:",comp_score)
                                    break

                                    



                            else:
                                print("Invalid. Try again.")
                            

                        else:
                            print("invalid. Try again.")
                coinflip_win_status_bowl_act()
                score_comp = comp_score

            if user_batting_done == True:
                def coinflip_win_status_bowl_act():

                    keywords = ['1','2','3','4','5','6','score']

                    comp_roll = ['1','2','3','4','5','6']

                    global comp_score
                    comp_score = 0
                    


                    print("The computer will be batting. Your objective is to match the computer's roll to knock it out.")

                    while True:
                        user_roll_bowl = input("Type a number from 1 to 6 ")

                        if  type(user_roll_bowl) == str:
                            if user_roll_bowl in keywords:
                                comp_choice_bat = random.choice(comp_roll)

                                if comp_choice_bat != user_roll_bowl and user_roll_bowl != "score":
                                    for char in comp_choice_bat:
                                            if char.isdigit():
                                                comp_score += int(char)
                                    print("You typed",user_roll_bowl,"and the computer rolled",comp_choice_bat)

                                elif user_roll_bowl == "score":
                                    print("The score is",comp_score)

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
                                    print("The total score was:",comp_score)
                                    break

                                    



                            else:
                                print("Invalid. Try again.")
                            

                        else:
                            print("invalid. Try again.")
                coinflip_win_status_bowl_act()
                score_comp = comp_score

            if user_bowling_done == True:
                def coinflip_win_status_bat_act():
                    
                    global user_score
                    user_score = 0


                    '1' == 1
                    '2' == 2
                    '3' == 3
                    '4' == 4
                    '5' == 5
                    '6' == 6



                    keywords = ['1','2','3','4','5','6','score']

                    comp_roll = ['1','2','3','4','5','6']

                    print("The computer will be bowling. Your objective is to keep scoring without typing a number that would match the computer's roll.")


                    while True:
                        user_roll = (input("Its your turn! Type a number from 1 to 6!"))

                        if type(user_roll) == str:

                            comp_choice = random.choice(comp_roll)

                            if user_roll in keywords:

                                if user_roll in keywords and user_roll != "score":
                                    for char in user_roll:
                                        if char.isdigit():
                                            user_score += int(char)
                                            print("You typed",user_roll)

                                if user_roll == "score":
                                    print("Your score is:",user_score)

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
                                    print("Your total score was:",user_score)
                                

                                    break

                            else:
                                print("Invalid. Try again.")
                                
                        else:
                            print("invalid. numbers are only alllowed.")
                coinflip_win_status_bat_act()
                score_bat = user_score

            print("computing the final results...")
            sleep(2)

            print("The score of the computer:",score_comp)
            print("And your score:",user_score)

            sleep(2)

            print("Therefore...")

            sleep(1)

            if score_comp > user_score:

                print("You lost!")

            elif score_comp < user_score:

                print("Congratulations!! You Won!")

            elif score_comp == user_score:
                print("You both got same scores! Fascinating!!")
        cric_hand_game()
    elif main_choice == "n":
        print("Have a nice day!")
        break

    else:
        print("Invalid input, Try again.")
