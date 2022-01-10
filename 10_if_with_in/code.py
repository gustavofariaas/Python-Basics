movies_watched = ["The Matrix", "Dumbo"]
user_input = input("Please enter the movie you've watched: ")

if user_input in movies_watched:
    print(f"You have already watched {user_input}")
else:
    print("This has been the first time you've watched this movie")