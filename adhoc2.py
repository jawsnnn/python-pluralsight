######
print("*****************************************************************")

def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]
    return sorted(strings, key=last_letter)

print(sort_by_last_letter(['This','is','a','local',' function']))
print("*****************************************************************")

print("Returning local functions")

def enclosing():
    def local_func():
        print("This is a returned local function")
    return local_func

lf = enclosing()
print("Hey", lf()) # OP: Hey None. Weird that function does not have a value itself but prints when called itself
lf()
print("*****************************************************************")
print("Closures")
# Closures is something that python creates for local functions so that returned local functions can 
# continue using variables defined in a scope that no longer exist e.g.

def enclosing():
    x = "This will be stored in a closure"
    i = 10
    def local_func():
        print(x, i)
    return local_func

lf = enclosing()
lf()
print(lf.__closure__)
print("*****************************************************************")

print("Implementation of local functions: Factories")
# Factory functions take variable inputs and combine them with local functions
# to provide flexible functionality

def raise_to(power):
    def local_func(x):
        return pow(x, power)
    return local_func

squared = raise_to(2)
print(squared(2))
print(squared(3))
print(squared(4))
cube = raise_to(3)
print(cube(2))
print(cube(3))
print(cube(4))
print("*****************************************************************")
print ("variable scopes")

message = "global"

def enclosing():
    message = "enclosing"

    def local_func():
        nonlocal message
        message="local"

    print ("Pre-local message is ", message)
    local_func()
    print ("Post-local message is ", message)

print("Pre-enclosing function message is", message)
enclosing()
print("Post-enclosing function message is", message)


print("*****************************************************************")
# Practical example of non-local scope

import time

def timer():
    last_called=None

    def time_elapsed():
        nonlocal last_called
        now = time.time()
        if last_called == None:
            last_called = now
            return None
        elapsed_time = now - last_called
        last_called = now
        return elapsed_time
    
    return time_elapsed
print("*****************************************************************")

# Example of decorator functions

def simple_func(x):
    string = "This is a simple function with "+str(x)+" decorations"
    return string

print(simple_func(0))

def decorator_func(f):
    def enhance(*args, **kwargs):
        res = f(*args, **kwargs)
        return "Decorations "+res+" More decorations"

    return enhance

@decorator_func
def simple_func(x):
    string = "This is a simple function with "+str(x)+" decorations"
    return string

print(simple_func(1))
