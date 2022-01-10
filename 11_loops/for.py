friends = ["Rolf", "Jen", "Bob", "Anne"]

for index in friends:
    print(f"{index} is my friend")

grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total +=grade

avarage = total/amount
print(f"The total of grades is {total} and the avarage is {avarage}.")