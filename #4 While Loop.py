'''
Take input from user from that time when he input a number which is less than five,
Otherwise the number is greater than 100 stop the program.
'''
while(True):
    user_input = int(input("Enter Your Number: "))
    if user_input < 100:
        print("Your number is less than 100\nTry Again!")
    elif user_input == 100:
        print("You enter exact \'100\', Input greatest number")
        continue
    else:
        print("Congratulations! your number is greater than 100")
        break
