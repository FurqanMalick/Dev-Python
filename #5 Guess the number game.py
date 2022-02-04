n = 44
no_of_guesses = 10
print("Guess the number between 1 to 50")
while (True):
    if no_of_guesses == 0:
        print("Game Over")
        break
    guess = int(input("Guess the number: "))
    if guess > n:
        print("Greater! Decrease Some")
        no_of_guesses = no_of_guesses - 1
        print("\n",no_of_guesses, "Attempt Left\n")
    elif guess < n:
        print("Lesser! Increase some")
        no_of_guesses = no_of_guesses - 1
        print("\n",no_of_guesses, "Attempt Left\n")
        continue
    else:
        print("Congratulations! You guess the hidden number in just", no_of_guesses, "Attempt")
        break
input("Press \'Y\' for Close")