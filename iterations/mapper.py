from decimal import Decimal
from functools import reduce

# map() takes a function and runs it over a sequence(s) of inputs generating another sequence with the outputs of the function

color = ['blue', 'white', 'grey']
animal = ['whale', 'monkey', 'man']
place = ['asian', 'european', 'mythical']

def combine (color, animal, place):
    return "{} colored {} {}".format(color, place, animal)

print(list(map(combine, color, animal, place)))

# filter() is similar to map in that it takes a single arg function and only returns those sequence numbers which are true (per the function)

def is_even(num):
    if Decimal(str(num)) % Decimal('2') == 0:
        return True
    else:
        return False

filtered = list(filter(is_even, [0, 1, 2, 3, 4, 5, 6]))

print(filtered)

# reduce takes a list/sequence and iterates over it, applying a single function to each value and accumulatiing the results 
# ultimately returning a single accumulated values. The first argument to the function is always the accumulated result by default
# and the second is the next list entry

l = [x for x in range(1,6)]

print(l)

def fact(x, y):
    print("{} into {}".format(x, y))
    return x * y 

ll = reduce(fact, l, 1)
print(ll)
