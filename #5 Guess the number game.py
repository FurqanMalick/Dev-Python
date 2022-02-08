from random import randrange
def game():
    n = randrange(1, 20)
    no_of_guesses = 10
    attempt = 1
    print("Guess the number between 1 to 50\n")
    while (True):
        if no_of_guesses == 0:
            print("Game Over")
            break
        guess = int(input("Guess the number: "))
        if guess > n:
            print("Greater! Decrease Some")
            no_of_guesses = no_of_guesses - 1
            attempt = attempt + 1
            print("\n",no_of_guesses, "Attempt Left\n")
            continue
        if guess < n:
            print("Lesser! Increase some")
            no_of_guesses = no_of_guesses - 1
            attempt = attempt + 1
            print("\n",no_of_guesses, "Attempt Left\n")
            continue
        if guess == n:
            print("Congratulations! You guess the hidden number in just", attempt, "Attempt\n")
            break
        return guess
    again()
def again():
    play_again = input("Press \'y\'for Play Again: ")
    play_again.upper()
    if play_again == "y":
        game()
    else:
        exit()
game()