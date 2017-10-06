# In this instance, the object is used as a decorator instead of the class
# e.g.


class Trace:
    def __init__(self):
        # Control if trace is enabled or not, default : True
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled is True:
                print("Calling function {}".format(f))
            return f(*args, **kwargs)
        return wrap

tracer = Trace()

def normal_func():
    print("a")

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]


print(type(rotate_list))
print(type(normal_func))

l = rotate_list([1,2,3,4])
print(l)

l = rotate_list([4,5,6])
print(l)

# Disabling function property does nothing
rotate_list.enabled = False

l = rotate_list([4,5,6])
print(l)

# Disabling object property disables tracing
tracer.enabled = False

l = rotate_list([4,5,6])
print(l)
