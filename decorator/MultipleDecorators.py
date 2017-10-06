def wrapper(f):
    def wrap(*args, **kwargs):
        print("Decorator 1. Args are {0} kwargs are {1}".format(args, kwargs))
        x = f(*args, **kwargs).upper()
        return x
    return wrap

class Trace:
    def __init__(self):
        print(" Object of class Trace initiated")
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled is True:
                print("Calling function {}".format(f))
            return f(*args, **kwargs)
        return wrap

tracer = Trace()

@tracer
@wrapper
def simple_func(name):
    return "This is a simple function. Name is {}".format(name)

print(simple_func('arpan'))
print(simple_func('abcd'))
print(simple_func('defgh'))
tracer.enabled = False
print(simple_func('Malviya'))
