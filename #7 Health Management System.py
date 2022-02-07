'''
DEVELOPED BY "FURQAN MALICK"
'''
# ---------------------------------------------------DATE AND TIME FUNCTION----------------------------------------------------------------------------
def gettime():
    import datetime
    now = datetime.datetime.now()
    timenow = now.strftime("%d-%m-%Y at %I:%M %p")
    return timenow

# ---------------------------------------------------START UPDATE FUNCTION----------------------------------------------------------------------------
# UPDATE FURQAN'S LOG
def updatefurqan():
    food_or_exercise = str(input("Press \'F\' for Update Furqan's \"Food\" & Press \'E\' for Update Furqan's \"Exercise\": "))

    if food_or_exercise == "F" or food_or_exercise == "f":      # For Food
        with open("Furqan Food.txt", "a") as f:
            food_eaten = str(input("Enter Food Name: "))
            time = gettime()
            f.write(str([str(time)]) + " Furqan eaten: " + food_eaten + "\n")
            print("\nFood log for Furqan successfully updated")

    elif food_or_exercise == "E" or food_or_exercise == "e":    # For Exercise
        with open("Furqan Exercise.txt", "a") as f:
            exercise_done = str(input("Enter Exercise Name: "))
            time = gettime()
            f.write(str([str(time)]) + " Furqan done: " + exercise_done + "\n")
            print("\nExercise log for Furqan successfully updated")

    else:
        print("Invalid Value!\nRemember you can only press \'F\' for \'Food\' & \'E\' for \'Exercise\'")
    return food_or_exercise

# UPDATE SHAKEEB'S LOG
def updateshakeeb():
    food_or_exercise = str(input("Press \'F\' for Update Shakeeb's \"Food\" & Press \'E\' for Update Shakeeb's \"Exercise\": "))

    if food_or_exercise == "F" or food_or_exercise == "f":  # For Food
        with open("Shakeeb Food.txt", "a") as f:
            food_eaten = str(input("Enter Food Name: "))
            time = gettime()
            f.write(str([str(time)]) + " Shakeeb eaten: " + food_eaten + "\n")
            print("\nFood log for Shakeeb successfully updated")

    elif food_or_exercise == "E" or food_or_exercise == "e":    # For Exercise
        with open("Shakeeb Exercise.txt", "a") as f:
            exercise_done = str(input("Enter Exercise Name: "))
            time = gettime()
            f.write(str([str(time)]) + " Shakeeb done: " + exercise_done + "\n")
            print("\nExercise log for Shakeeb successfully updated")

    else:
        print("Invalid Value!\nRemember you can only press \'F\' for \'Food\' & \'E\' for \'Exercise\'")
    return food_or_exercise

# UPDATE SAAD'S LOG
def updatesaad():
    food_or_exercise = str(input("Press \'F\' for Update Saad's \"Food\" & Press \'E\' for Update Saad's \"Exercise\": "))

    if food_or_exercise == "F" or food_or_exercise == "f":  # For Food
        with open("Saad Food.txt", "a") as f:
            food_eaten = str(input("Enter Food Name: "))
            time = gettime()
            f.write(str([str(time)]) + " Saad eaten: " + food_eaten + "\n")
            print("\nFood log for Saad successfully updated")

    elif food_or_exercise == "E" or food_or_exercise == "e":    # For Exercise
        with open("Saad Exercise.txt", "a") as f:
            exercise_done = str(input("Enter Exercise Name: "))
            time = gettime()
            f.write(str([str(time)]) + " Saad done: " + exercise_done + "\n")
            print("\nExercise log for Saad successfully updated")

    else:
        print("Invalid Value!\nRemember you can only press \'F\' for \'Food\' & \'E\' for \'Exercise\'")
    return food_or_exercise
# ---------------------------------------------------END UPDATE FUNCTION----------------------------------------------------------------------------

# ---------------------------------------------------START LOG FUNCTION----------------------------------------------------------------------------

# LOG FURQAN

def logfurqan():
    food_or_exercise = str(input("Press \'F\' for Furqan's Log \"Food\" & Press \'E\' for Furqan's Log \"Exercise\": "))

    if food_or_exercise == "F" or food_or_exercise == "f":  # For Food
        content = open("Furqan Food.txt")
        f = content.read()
        print(f)
    elif food_or_exercise == "E" or food_or_exercise == "e":  # For Exercise
        content = open("Furqan Exercise.txt")
        f = content.read()
        print(f)
    else:
        print("Invalid Value!\nRemember you can only press \'F\' for \'Food\' & \'E\' for \'Exercise\'")
    return food_or_exercise

# LOG SHAKEEB

def logshakeeb():
    food_or_exercise = str(input("Press \'F\' for Shakeeb's Log\"Food\" & Press \'E\' for Shakeeb's Log\"Exercise\": "))

    if food_or_exercise == "F" or food_or_exercise == "f":      # For Food
        content = open("Shakeeb Food.txt")
        f = content.read()
        print(f)
    elif food_or_exercise == "E" or food_or_exercise == "e":    # For Exercise
        content = open("Shakeeb Exercise.txt")
        f = content.read()
        print(f)
    else:
        print("Invalid Value!\nRemember you can only press \'F\' for \'Food\' & \'E\' for \'Exercise\'")
    return food_or_exercise

# LOG SAAD

def logsaad():
    food_or_exercise = str(input("Press \'F\' for Saad's Log\"Food\" & Press \'E\' for Saad's Log\"Exercise\": "))

    if food_or_exercise == "F" or food_or_exercise == "f":      # For Food
        content = open("Saad Food.txt")
        f = content.read()
        print(f)
    elif food_or_exercise == "E" or food_or_exercise == "e":    # For Exercise
        content = open("Saad Exercise.txt")
        f = content.read()
        print(f)
    else:
        print("Invalid Value!\nRemember you can only press \'F\' for \'Food\' & \'E\' for \'Exercise\'")
    return food_or_exercise

# ---------------------------------------------------END LOG FUNCTION----------------------------------------------------------------------------

# ---------------------------------------------------START OF PROGRAM----------------------------------------------------------------------------
while (True):
    client_id = int(input("Press \'1\' for \"Furqan\", \tPress \'2\' for \"Shakeeb\",\tPress \'3\' for \"Saad\": "))
    update_or_log = int(input("Press \'1\' for \"update data\" & Press \'2\' for \"see log\": "))

    # UPDATE--------------------
        # FOR FURQAN
    if client_id == 1 and update_or_log == 1:    # (client id == "Furqan") and (update_or_log == update data)
        updatefurqan()
        continue
    # FOR SHAKEEB
    elif client_id == 2 and update_or_log == 1: # (client id == "Shakeeb") and (update_or_log == update data)
        updateshakeeb()
        continue
    # FOR SAAD
    elif client_id == 3 and update_or_log == 1: # (client id == "Saad") and (update_or_log == update data)
        updatesaad()
        continue
    # LOG--------------------

    # FOR FURQAN
    elif client_id == 1 and update_or_log == 2:   # (client id == "Furqan") and (update_or_log == See Log)
        logfurqan()
        continue
    # For FOR SHAKEEB
    elif client_id == 2 and update_or_log == 2: # (client id == "Shakeeb") and (update_or_log == See Log)
        logshakeeb()
        continue
    # For FOR SHAKEEB
    elif client_id == 3 and update_or_log == 2:     # (client id == "Saad") and (update_or_log == See Log)
        logsaad()
        continue

    else:
        print("Invalid Value!\nYou can press only[1, 2, 3] for client & [1, 2] for update and log")
        break