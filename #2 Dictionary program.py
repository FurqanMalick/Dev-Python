lst = {
    "computer":"computer is an electronic machine",
    "program": "A program is a set of instruction",
    "algorithm":"Algorithm is a set of steps",
    "python":"Python is a programming language"
}
x = "YOU CAN ONLY SEARCH\nCOMPUTER, PROGRAM, ALGORITHM, PYTHON"
print(x)
search = input("Search your desired definition: ")
print("The correct definition is: ", lst[search])