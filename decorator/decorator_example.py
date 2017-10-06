
"""
This script shows one way of making decorators parameterized
In normal course, decorators always take a callable and return a callable
Here we create an enclosing function that implemennts the decorator in a parameterized way and returns it
"""

import functools

# This is not a decorator. This is a function that takes a string case as an argument and returns a decorator
# for that case
def validate_case_arg(string_case):

    # This is the decorator
    def validator(f):

        @functools.wraps(f)
        def wrap(*args):
            for i in args:
                if i.upper() != i:
                    if string_case == "upper":
                        raise ValueError("{} is already in room voice".format(i))
                else:
                    if string_case == "lower":
                        raise ValueError("{} is already in stadium talk".format(i))
            f(*args)                    
        return wrap
    # Return the decorator
    return validator


# validate_case_arg is not a decorator. This is a function that returns a decorator for upper case (see above)
@validate_case_arg('upper')
def room_voices(hesaid):
    "Lowers voices shouted in a room"
    print(hesaid.lower())

# validate_case_arg is not a decorator. This is a function that returns a decorator for lower case (see above)
@validate_case_arg("lower")
def stadium_talk(shesaid):
    "Raises volume in a stadium"
    print(shesaid.upper())


