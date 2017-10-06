print("Good**********************************************")

def hello():
    "Print a well known message"
    print("Hello World!")

hello()
print(hello.__name__)
print(hello.__doc__)
help(hello)


print("Bad**********************************************")
def dummy_decorator(f):
    def wrap(*args, **kwargs):
        return f(*args, **kwargs)
    return wrap

@dummy_decorator
def hello2():
    "Print a well known message"
    print("Hello World!")

hello2()
print(hello2.__name__)
print(hello2.__doc__)
help(hello2)

# Ugly workaround

print("Workaround1**********************************************")

def dummy_decorator3(f):
    def wrap(*args, **kwargs):
        wrap.__name__ = f.__name__
        wrap.__doc__ = f.__doc__
        return f(*args, **kwargs)
    return wrap

@dummy_decorator3
def hello3():
    "Print a well known message"
    print("Hello World!")

hello3()
help(hello3)

# Standard workaround

print("Workaround 2 STANDARD**********************************************")
import functools
def dummy_decorator4(f):
    @functools.wraps(f)
    def wrap(*args, **kwargs):
        return f(*args, **kwargs)
    return wrap

@dummy_decorator4
def hello4():
    "Print a well known message"
    print("Hello World!")

hello4()
help(hello4)
