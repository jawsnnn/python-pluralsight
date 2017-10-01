# Lambda functions

list_a = ['a z', 'b y', 'c x']
print ("Normal sort")
print(sorted(list_a))

print ("Sorted on last name")
print(sorted(list_a, key = lambda name: name.split()[-1]))

print("Lambda returns a function object")

last_name = lambda name: name.split()[-1]

print(last_name)

print(last_name("Arpan ANON Malviya"))

print("********************************************************************************************")

# Callable objects

def this_func():
    return 0

print("Functions are callable")
print(callable(this_func))


print("Lambda Functions are callable")
print(callable(lambda name: name.split()[0]))


print("Classes are callable")
print(callable(list))


print("Class functions are callable")

x = [0, 1, 2, 3]

print(callable(x.pop))

print("Objects are not callable")
x = []
print(callable(x))

print("Objects are callable if the class is declared with a __call__ method")
class Callable_a:
    def __call__(self):
        print("Called")

x = Callable_a()
x()
print(callable(x))

print("********************************************************************************************")

# Formal Arguments

print("This is a demonstration of hypervolume")
def hypervolume(*args):
    print(type(args))
    v = 1
    for i in args:
        v*= i
    return v

print("Volume of rectangle 2 by 4: {}", hypervolume(2, 4))
print("Volume of cuboid 2 by 4 by 5: {}", hypervolume(2, 4, 5))
print("Volume of hyper-cuboid 2 by 4 by 5 by 10: {}", hypervolume(2, 4, 5 ,10))
print("Volume of single dimension line 4: {}", hypervolume(4))
print("Volume of nothing is reported incorrectly as {} ", hypervolume())

print("********************************************************************************************")

# To fix this, we can specify at least one arg in the function definition and take the rest as variables
# Also args is not a keyword. Note the different variable name in the declaration below

def hypervolume(arg, *lengths):
    v = arg
    for i in lengths:
        v*= i
    return v


print("Volume of rectangle 2 by 4: {}", hypervolume(2, 4))
print("Volume of cuboid 2 by 4 by 5: {}", hypervolume(2, 4, 5))
print("Volume of hyper-cuboid 2 by 4 by 5 by 10: {}", hypervolume(2, 4, 5 ,10))
print("Volume of single dimension line 4: {}", hypervolume(4))
try:
    print("This will return in a predicatble error{} ", hypervolume())
except Exception as e:
    print(e)
print("********************************************************************************************")

# Demonstration of keyword args and args

t = (1, 2 ,3, 4, 5)

def print_args(a, b, *c):
    print(a)
    print(b)
    # *c soaks up remaining values
    print(c)

# Call with unpacked tuple

print_args(*t)

d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

def print_args(a, b, **D):
    print(a)
    print(b)
    print(D)

print_args(**d)


print("********************************************************************************************")

print("Passing arguments")

def trace(fn, *b, **c):
    print("Function is",fn)
    print("Is Callable?: ", callable(fn))
    print("Positional Arguments", b)
    print("Keyword arguments",c)
    result = fn(*b, **c)
    print(result)

trace(int, "ff", base=16)
print("********************************************************************************************")

print ("Transposing lists using *args")

list_a=[1,2,3,4]
list_b=[5,6,7,8]
list_c=[11,22,33,44]
print("Original lists")
print(list_a)
print(list_b)
print(list_c)

list_all=[list_a, list_b, list_c]
print (list_all)
print ("Transposed list")
# Note that this notation is very common to transpose iterables
transposed = list(zip(*list_all))
print(transposed)


