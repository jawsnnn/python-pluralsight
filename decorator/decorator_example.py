def validate_case_arg(string_case):
    def validator(f):
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
    return validator

@validate_case_arg('upper')
def room_voices(hesaid):
    print(hesaid.lower())

@validate_case_arg("lower")
def stadium_talk(shesaid):
    print(shesaid.upper())


