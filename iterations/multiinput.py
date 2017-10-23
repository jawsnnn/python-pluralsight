# Single input


l = [i for i in range (10)]

print(l)
print(type(l))
print(dir(l))

# Multi-input

l = [(x, y, z) for x in range(5) for y in range(3)  for z in range (10)]

print (l)

l = [ (x ,y) for x in range(100) if x > 50 for y in range(100) if x != y ]

#print (l)

# This is equivalent to 

l = []

for x in range(100):
    if x > 50:
        for y in range(100):
            if x != y:
                l.append((x,y))

print(l)

l = [(x,y) for x in range(5) for y in range(x)]
print("**********************************************************************")
print (l)

for x in range(5):
    print(x)
    for y in range(x):
        print(y)
    print("--")


print("**********************************************************************")
# Nested comprehensions

l = [[y* 3 for y in range(x)] for x in range(10)]

print (l)
