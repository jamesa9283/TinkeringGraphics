import random

randomNumber = random.randrange(0, 100)
guessed = False


def check_guess(current_input):
    if current_input == randomNumber:
        print("Well done!")
    elif current_input > 100:
        print("Our guess range is between 0 and 100, please try a bit lower")
    elif current_input < 0:
        print("Our guess range is between 0 and 100, please try a bit higher")
    elif current_input > randomNumber:
        print("Try one more time, a bit lower")
    elif current_input < randomNumber:
        print("Try one more time, a bit higher")


while not guessed:
    userInput = int(input("Your guess please: "))
    check_guess(userInput)
print("You win!")
