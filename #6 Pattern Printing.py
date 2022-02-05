def game():
    i = 1
    no_of_rows = int(input("Enter number of rows: "))
    pattern = int(input("Press 1 for Ascending & 0 for Descending: "))
    while True:
        if pattern != 1 and pattern != 0:
            print("Please enter \'1\' for Ascending order & \'0\' for Descending order: ")
            break
        elif (pattern == 1) and (i <= no_of_rows):
            print("* " * i)
            i = i + 1
        elif (pattern == 0) and (no_of_rows >= i):
            print("* " * no_of_rows)
            no_of_rows = no_of_rows - 1
        else:
            break
    again()

def again():
    play_again = input("\nPress \'y\'for Play Again else exit: ")
    if play_again == "y" or play_again == "Y":
        print("\n")
        game()
    else:
        exit()

game()