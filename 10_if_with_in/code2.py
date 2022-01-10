number = 7
user_play = input("Press 'y' if you want to play: ").lower()

if user_play == "y":
    user_number = int(input("Please enter a number: "))
    if user_number == number:
        print("You have enter the correct number")
    elif abs(user_number - number) == 1:
        print("You miss by one number")
    else:
        print("You got the wrong number")