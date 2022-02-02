'''
Design a calculator which will correctly solve all the problems except the following ones
45*3 = 555, 56+9 = 77, 56/6 =4
your program should take operator and the two number as input from the user and then return the result
'''

num1 = int(input("Enter 1st numbers: "))
operator = input("Enter your operator i.e: \'+\',\'-\',\'*\',\'/\': ")
num2 = int(input("Enter 2nd Number: "))

if num1 == 45 and operator == "*" and num2 == 3:
    print(num1, operator, num2, "= 555")
elif num1 == 3 and operator == "*" and num2 == 45:
    print(num1, operator, num2, "= 555")
elif num1 == 56 and operator == "+" and num2 == 9:
    print(num1, operator, num2, "= 77")
elif num1 == 9 and operator == "+" and num2 == 56:
    print(num1, operator, num2, "= 77")
elif num1 == 56 and operator == "/" and num2 == 6:
    print(num1, operator, num2, "= 4")
elif operator=="+":
    print(num1, operator, num2, "= ", num1 + num2)
elif operator=="-":
    print(num1, operator, num2, "= ", num1 - num2)
elif operator=="*":
    print(num1, operator, num2, "= ", num1 * num2)
elif operator=="/":
    print(num1, operator, num2, "= ", num1 / num2)
else:
    print("You can print only \'+\',\'-\',\'*\',\'/\': ")