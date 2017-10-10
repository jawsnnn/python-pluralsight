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
        result = Shipping.next_serial
        Shipping.next_serial += 1
        return result

    def __init__(self, type_code, contents):
        self.type_code = type_code
        self.contents = contents
        self.serial = ClassContainer._get_serial_num()


# Usage of classmethods: Creation of named constructors

class Shipping:

    next_serial = 1337

    @classmethod
    def _get_next_serial_num(cls):
        Shipping.next_serial += 1
        return Shipping.next_serial

    @classmethod
    def _get_bic_code(cls, owner_code, serial):
        return owner_code+'U'+str(serial).zfill(6)

    @classmethod
    def create_empty(cls, owner_code, *args, **kwargs):
        return cls(owner_code, contents = None, *args, **kwargs)

    @classmethod
    def create_with_list(cls, owner_code, items, *args, **kwargs):
        return cls(owner_code, contents = list(items), *args, **kwargs)

    # This can be easily overwritten
    def non_static(self):
        print("This is a shipping container")

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        # Polymorphism does not work with static methods
        self.bic = self._get_bic_code(owner_code = self.owner_code,
                serial = Shipping._get_next_serial_num())

class RefrigeratedShipping(Shipping):

    MAX_CELSIUS = 4.0

    # This is overridden without any issues
    def non_static(self):
        print("This is a refrigerated shipping container")

    # This will need to be called with the instant reference (self)
    # in base class
    # Polymorphism does not work with static methods
    
    @staticmethod
    def _get_bic_code(owner_code, serial):
        return owner_code+'R'+str(serial).zfill(6) 

    def __init__(self, owner_code, contents, celsius):
        super().__init__(owner_code, contents)
        if celsius > RefrigeratedShipping.MAX_CELSIUS:
            raise ValueError("celsius value supplied cannot be greater than %", RefrigeratedShipping.MAX_CELSIUS)
        self.celsius = celsius
