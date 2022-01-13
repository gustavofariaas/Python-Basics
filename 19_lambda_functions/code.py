def add(x,y):
    return x + y

print(add(2,3))

## Using lambda

add2 = lambda x,y: x+y

print(add2(2,3))

print((lambda x,y: x+y)(2,6))

## Another way to use lambda

sequence = [1,3,5,9]
doubled = [(lambda x:x * 2)(x) for x in sequence]
print(doubled)
#or
doubled = list(map(lambda x:x * 2,sequence))
print(doubled)

