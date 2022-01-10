number = 7

while True:
    user_play = input("Would you like to play? (y/n): ").lower()

    if user_play == "n":
        print("See ya!")
        break

    user_number = int(input("Please enter a number: "))
    if user_number == number:
        print("You have enter the correct number")
    elif abs(user_number - number) == 1:
        print("You miss by one number")
    else:
        print("You got the wrong number")
