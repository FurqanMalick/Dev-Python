import random
def dual_player_game():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # RANDOM CHOICE FOR SNAKE, WATER, GUN
    def randomfunction1():
        lst_swg = ["S", "W", "G"]
        rand_var = random.choice(lst_swg)
        return rand_var

    def randomfunction2():
        lst_swg = ["S", "W", "G"]
        rand_var = random.choice(lst_swg)
        return rand_var

    def player1():
        while True:
            try:
                name_input1 = str(input("Enter First Player Name: "))
                break
            except ValueError:
                print("Invalid Name! Try Again\n")
                continue
        return name_input1.upper()

    def player2():
        while True:
            try:
                name_input2 = str(input("Enter Second Player Name: "))
                break
            except ValueError:
                print("Invalid Name! Try Again\n")
                continue
        return name_input2.upper()

    first_player_name = player1()
    second_player_name = player2()

    def round():
        while True:
            try:
                x = int(input("\nHow many rounds you both want to play: "))
                break
            except ValueError:
                print('You entered a non integer value, try again.\n')
                continue
        return int(x)

    def choose1():
        while True:
            try:
                x = int(input(f"\n{first_player_name} Please Choose a number between 1 to 9: "))  # 1st USER INPUT
                if x in lst:
                    break
                else:
                    print(f"Dear {first_player_name}!You can only select a number between 1 to 9! ENTER AGAIN: ")
                    continue
            except ValueError:
                print(f"Dear {first_player_name}!You can only select a number between 1 to 9! ENTER AGAIN: ")
                continue
        return int(x)

    def choose2():
        while True:
            try:
                x = int(input(f"{second_player_name} Please Choose a number between 1 to 9: "))  # 1st USER INPUT
                if x in lst:
                    break
                else:
                    print(f"Dear {second_player_name}!You can only select a number between 1 to 9! ENTER AGAIN: ")
                    continue
            except ValueError:
                print(f"Dear {second_player_name}!You can only select a number between 1 to 9! ENTER AGAIN: ")
                continue
        return int(x)



    # FUNCTION TO START GAME
    def gamedual():
        i = 1
        first_win = 0
        second_win = 0
        game_draw = 0

    # Players Name
        print(f"\nThe game will be played between {first_player_name} and {second_player_name}")
        g_round = round()


        while i <= g_round:
            first_player_choice = choose1()
            second_player_choice = choose2()
            first_random = randomfunction1()
            second_random = randomfunction2()
            if first_player_choice and second_player_choice in lst:
                try:
            # SNAKE
                    if (first_random == "S") and (second_random == "S"):
                        print(f"\n{first_player_name} select \'Snake\' & {second_player_name} also select \'Snake\'\n\t\t\t\t\t\t\t\tGAME DRAW!")
                        game_draw += 1
                        i += 1
                        continue
                    elif (first_random == "S") and (second_random == "W"):
                        print(f"\n{first_player_name} select \'Snake\' & {second_player_name} select \'Water\'\n{first_player_name}'s Snake drink {second_player_name}'s Water.\t\t\t\t{first_player_name} is Winner!")
                        first_win +=1
                        i += 1
                        continue
                    elif (first_random == "S") and (second_random == "G"):
                        print(f"\n{first_player_name} select \'Snake\' & {second_player_name} select \'Gun\'\n{second_player_name}'s Gun shoot {first_player_name}'s Snake.\t\t\t\t{second_player_name} is Winner!")
                        second_win += 1
                        i += 1
                        continue

                # WATER
                    elif (first_random == "W") and (second_random == "S"):
                        print(f"\n{first_player_name} select \'Water\' & {second_player_name} select \'Snake\'\n{second_player_name}'s Snake sink in {first_player_name}'s Water.\t\t\t\t{first_player_name} is Winner!")
                        first_win += 1
                        i += 1
                        continue
                    elif (first_random == "W") and (second_random == "W"):
                        print(f"\n{first_player_name} select \'Water\' & {first_player_name} also select \'Water\'\n\t\t\t\t\t\t\t\tGAME DRAW!")
                        game_draw += 1
                        i += 1
                        continue
                    elif (first_random == "W") and (second_random == "G"):
                        print(f"\n{first_player_name} select \'Water\' & {second_player_name} select \'Gun\'\n{second_player_name}'s Gun sink in {first_player_name}'s Water.\t\t\t\t{first_player_name} is Winner!")
                        first_win += 1
                        i += 1
                        continue

                # GUN
                    elif (first_random == "G") and (second_random == "S"):
                        print(f"\n{first_player_name} select \'Gun\' & {second_player_name} select \'Snake\'\n{first_player_name} Gun shoot {second_player_name}'s Snake.\t\t\t\t{first_player_name} is Winner!!")
                        first_win += 1
                        i += 1
                        continue
                    elif (first_random == "G") and (second_random == "W"):
                        print(f"\n{first_player_name} select \'Gun\' & {second_player_name} select \'Water\'\n{first_player_name} Gun sink in {second_player_name}'s Water.\t\t\t\t{second_player_name} is Winner!")
                        second_win += 1
                        i += 1
                        continue
                    elif (first_random == "G") and (second_random == "G"):
                        print(f"\n{first_player_name} select \'Gun\' & {second_player_name} also select \'Gun\'\n\t\t\t\t\t\t\t\tGAME DRAW!")
                        game_draw += 1
                        i += 1
                        continue
                    break
                except ValueError:
                    print("\n\t\t\t\t\t\t\tInvalid Entry!\n\t\t\t\t\tSelect again carefully")
                    continue

        # WINNER ANNOUNCEMENT
        if second_win > first_win:
            print(f"\nCONGRATULATIONS {second_player_name}! You are Winner\n{second_player_name}'s score is: {second_win}")
            print(f"\n{first_player_name} score only {first_win}")
        elif first_win > second_win:
            print(f"\nCONGRATULATIONS {first_player_name}! You are Winner\n{first_player_name}'s score is: {first_win}")
            print(f"\n{second_player_name} score only {second_win}")
        else:
            print(f"OOPS! {first_player_name}'s score is {first_win} & {second_player_name}'s score is also {second_win}\t\t\t The game is drawn")
        print(f"\n{game_draw} times game drawn")

    gamedual()