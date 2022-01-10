numbers = [1, 2, 3]
multi = [ number * 2 for number in numbers]

print(multi)

friends = ["Bob", "Sam", "Son", "Sonia", "Jack"]
starts_s = [friend for friend in friends if friend.startswith("S")]

print(starts_s)