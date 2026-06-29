import random


while True:
    try:
        number_input = int(input("choose number of 1of10: and 0=Exit:"))
    except ValueError:
        print("please enter a valid number")
        continue
    if number_input == 0:
        break
    random_number = random.randint(1,10)
    if number_input > 10 or number_input <= 0:
        print("please choose between 1of10")
    elif random_number == number_input:
        print(f"you win, computer choose:{random_number}")
    elif number_input != random_number:
        print(f"you lost, computer choose:{random_number}")