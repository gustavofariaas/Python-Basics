users = [
    (0, "Bob", "password"),
    (1,"Rolf", "bob123"),
    (2, "Jose", "longpassword"),
    (3, "username", "1234")
]
#user[1] is key and user is value  user[1]: user vai ser o inicio da String -> Bob: (informaçoes do user), Bob se transforma da Key
username_mapping = {user[1]: user for user in users}

print(username_mapping)
print(username_mapping["Bob"])  # (0, "Bob", "password")

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your password is correct")
else:
    print("Your password is wrong")