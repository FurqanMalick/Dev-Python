import random
txt = "SNAKE, WATER, GUN GAME\nDEVELOPED BY ***FURQAN MALICK***\n"
new_str = txt.center(50)
print(new_str)

# RANDOM CHOICE FOR SNAKE, WATER, GUN
def randomfunction():
    lst_swg = ["Snake", "Water", "Gun"]
    rand_var = random.choice(lst_swg)
    return rand_var

# FUNCTION FOR INPUT USER NAME
def inputname():
    name = str(input("Enter player's name = "))
    user_name = name.capitalize()
    return user_name

# FUNCTION TO START GAME
def game():
    i = 1
    player_win = 0
    computer_win = 0
    game_draw = 0

    while True:
        try:
            gameround = int(input("How many rounds you want to play with computer: "))
            break
        except ValueError:
            print('You entered a non integer value, try again.\n')
            continue

    while i <= gameround:
        computer_choice = randomfunction()      #COMPUTER CHOOSE RANDOMLY ONE WORD
        game_var = str(input("\nPress \'S\' for SNAKE, Press \'W\' for WATER & Press \'G\'for GUN: "))      #USER INPUT

    # SNAKE
        if (game_var == "S" or game_var == "s") and computer_choice == "Snake":
            print("You select \'Snake\' & Computer also select \'Snake\'\n\t\t\t\t\t\t\t\tGAME DRAW!")
            game_draw += 1
            i += 1
            continue
        elif (game_var == "S" or game_var == "s") and computer_choice == "Water":
            print("You select \'Snake\' & Computer select \'Water\'\nYour Snake drink Computer's Water.\t\t\t\tYOU ARE WINNER!")
            player_win += 1
            i += 1
            continue
        elif (game_var == "S" or game_var == "s") and computer_choice == "Gun":
            print("You select \'Snake\' & Computer select \'Gun\'\nComputer's Gun shoot Your Snake.\t\t\t\tCOMPUTER IS WINNER!")
            computer_win += 1
            i += 1
            continue

    # WATER
        elif (game_var == "W" or game_var == "w") and computer_choice == "Snake":
            print("You select \'Water\' & Computer select \'Snake\'\nComputer's Snake sink in Your Water.\t\t\t\tYOU ARE WINNER!")
            player_win += 1
            i += 1
            continue
        elif (game_var == "W" or game_var == "w") and computer_choice == "Water":
            print("You select \'Water\' & Computer also select \'Water\'\n\t\t\t\t\t\t\t\tGAME DRAW!")
            game_draw += 1
            i += 1
            continue
        elif (game_var == "W" or game_var == "w") and computer_choice == "Gun":
            print("You select \'Water\' & Computer select \'Gun\'\nComputer's Gun sink in Your Water.\t\t\t\tYOU ARE WINNER!")
            player_win += 1
            i += 1
            continue

    # GUN
        elif (game_var == "G" or game_var == "g") and computer_choice == "Snake":
            print("You select \'Gun\' & Computer select \'Snake\'\nYour Gun shoot Computer's Snake.\t\t\t\tYOU ARE WINNER!")
            player_win += 1
            i += 1
            continue
        elif (game_var == "G" or game_var == "g") and computer_choice == "Water":
            print("You select \'Gun\' & Computer select \'Water\'\nYour Gun sink in Computer's Water.\t\t\t\tCOMPUTER IS WINNER!")
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
        print(f"\nLOOSER! Computer is Winner\nIt's score is: {computer_win}")
        print(f"{player_name} score only {player_win}")
    elif player_win > computer_win:
        print(f"\nCONGRATULATIONS! {player_name} is Winner and the score is: {player_win}")
        print(f"Computer score only {computer_win}")
    else:
        print(f"OOPS! {player_name}'s score is {player_win} & Computer's score is also {computer_win}\t\t\t The game is drawn")
    print(f"\n{game_draw} times game drawn")

# START GAME
while (True):
    player_name = inputname()
    if player_name.isalpha():
        game()
        break
    else:
        print("invalid Name! TRY AGAIN")
        continue