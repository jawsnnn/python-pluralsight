# Note: All three implementations are functionally equivalent

# Demo for class attributes : 1

class ShippingContainer:

    next_serial = 1227

    def __init__(self, type_code, contents):

        self.type_code = type_code
        self.contents = contents
        self.serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1

# Demo for class attributes : 2
class Container:

    next_serial = 1337
   

    # NOTE: The staticmethod decorator does not really add anything here
    @staticmethod
    def _get_serial_num():
        result = Container.next_serial
        Container.next_serial += 1
        return result

    def __init__(self, type_code, contents):
        self.type_code = type_code
        self.contents = contents
        self.serial = Container._get_serial_num()


# Demo for class attributes: 3
# Using classmethod


class ClassContainer:

    next_serial = 1337
   

    # NOTE: The staticmethod decorator does not really add anything here
    @classmethod
    def _get_serial_num(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    def __init__(self, type_code, contents):
        self.type_code = type_code
        self.contents = contents
        self.serial = ClassContainer._get_serial_num()


# Usage of classmethods: Creation of named constructors

class Shipping:


    @classmethod
    def create_empty(cls, typ):
        return cls(typ, contents = None)

    @classmethod
    def create_with_list(cls, typ, items):
        return cls(typ, contents = list(items))

    def __init__(self, typ, contents):
        self.type_code = typ
        self.contents = contents
