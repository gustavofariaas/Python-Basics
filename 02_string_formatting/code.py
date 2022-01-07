name = "Bob"
greetings = f"Hello, {name}"

print(greetings)

name = "Gustavo"
greetings = "Hello, {}"

with_name = greetings.format(name)
with_name2 = greetings.format("Joao")

print(with_name)
print(with_name2)

longer_phrase  = "Hello {}, today is {}"
formatted = longer_phrase.format("Gustavo", "Tuesday")
print(formatted)