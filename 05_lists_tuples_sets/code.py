list = ["Bob", "Ana", "John"]
tuple = ("Bob", "Ana", "John")
set = {"Bob", "Ana", "John"}

# We cannot access set, it not allows to be subscriptabled
print(tuple)

list[0] = "Smith"
print(list)

# tuple[0] = "Smith" - isso vai dar erro, nao pode alterar valor em tuple

# you cant add a value in a tuple
list.append("Bob")
print(list)

set.add("Smith")
print(set)

set.remove("Bob")
list.remove("Bob")
print(set, list)