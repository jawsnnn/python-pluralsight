"""
Factory classs demo
Function is passed to decorator class
Decorator class must implement the __call__ method for this to work
demoCallCount is passed to __init__ as f
calling the function actually calls the __call__ method which increments the count and then calls the original function
What object is being used???
"""

class CallCount:
    def __init__(self, f):
        self.f = f
        print("Object initiated")
        print(type(self))
        self.count=0

    def __call__(self, *args, **kwargs):
        self.count+=1
        return self.f(*args, **kwargs)

class dummy:
    def __init__(self):
        print("dummy object created")
        print(type(self))

@CallCount
def demoCallCount():
    print("This is a call")

