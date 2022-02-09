'''
#Problem
Make a program by using while loop for 10 times and run SNAKE, WATER, GUN game
'''
import random


def randomfunction():
    lst_swg = ["Snake", "Water", "Gun"]
    rand_var = random.choice(lst_swg)
    return rand_var


# name = str(input("Enter player's name = "))

# Game Function
def inputname():
    name = str(input("Enter player's name = "))
    name.capitalize()
    return name


def game():
    i = 1
    player_win = 0
    computer_win = 0
    game_draw = 0
    number_of_game = int(input("How many times you want to play this game with computer: "))

    while i <= number_of_game:
        computer_choice = randomfunction()
        # print(computer_choice)
        game_var = str(input("\nPress \'S\' for SNAKE, Press \'W\' for WATER & Press \'G\'for GUN: "))

    # SNAKE
        if (game_var == "S" or game_var == "s") and computer_choice == "Snake":
            print("You select \'Snake\' & Computer also select \'Snake\'\n\t\t\t\t\t\t\t\tGAME DRAW!")
            game_draw += 1
            i += 1
            continue
        elif (game_var == "S" or game_var == "s") and computer_choice == "Water":
            print("You select \'Snake\' & Computer select \'Water\'\nSnake drinks Water.\t\t\t\tYOU ARE WINNER!")
            player_win += 1
            i += 1
            continue
        elif (game_var == "S" or game_var == "s") and computer_choice == "Gun":
            print("You select \'Snake\' & Computer select \'Gun\'\nGun shoot Snake.\t\t\t\tCOMPUTER IS WINNER!")
            computer_win += 1
            i += 1
            continue

    # WATER
        elif (game_var == "W" or game_var == "w") and computer_choice == "Snake":
            print("You select \'Water\' & Computer select \'Snake\'\nSnake sink in Water.\t\t\t\tYOU ARE WINNER!")
            player_win += 1
            i += 1
            continue
        elif (game_var == "W" or game_var == "w") and computer_choice == "Water":
            print("You select \'Water\' & Computer also select \'Water\'\n\t\t\t\t\t\t\t\tGAME DRAW!")
            game_draw += 1
            i += 1
            continue
        elif (game_var == "W" or game_var == "w") and computer_choice == "Gun":
            print("You select \'Water\' & Computer select \'Gun\'\nGun sink in Water.\t\t\t\tYOU ARE WINNER!")
            player_win += 1
            i += 1
            continue

    # GUN
        elif (game_var == "G" or game_var == "g") and computer_choice == "Snake":
            print("You select \'Gun\' & Computer select \'Snake\'\nGun shoot Snake.\t\t\t\tYOU ARE WINNER!")
            player_win += 1
            i += 1
            continue
        elif (game_var == "G" or game_var == "g") and computer_choice == "Water":
            print("You select \'Gun\' & Computer select \'Water\'\nGun sink in Water.\t\t\t\tCOMPUTER IS WINNER!")
            computer_win += 1
            i += 1
            continue
        elif (game_var == "G" or game_var == "g") and computer_choice == "Gun":
            print("You select \'Gun\' & Computer also select \'Gun\'\n\t\t\t\t\t\t\t\tGAME DRAW!")
            game_draw += 1
            i += 1
            continue
        else:
            print("\n\t\t\t\t\t\t\tInvalid Entry!\n\t\t\t\t\tSelect again carefully")

    # WINNER ANNOUNCEMENT
    if computer_win > player_win:
        print(f"\nLOOSER! Computer is Winner\nit's score is: {computer_win}")
        print(f"{player_name} score only {player_win}")
    elif player_win > computer_win:
        print(f"\nCONGRATULATIONS! {player_name} is Winner and the score is: {player_win}")
        print(f"Computer score only {computer_win}")
    else:
        print(f"OOPS! {player_name}'s score is {player_win} & Computer's score is also {computer_win}\t\t\t The game is drawn")
    print(f"\n{game_draw} times game drawn")


while (True):
    player_name = inputname()
    if player_name.isalpha():
        game()
    else:
        print("invalid name format! TRY AGAIN")
        continue
print("press \'E\' for Exit")