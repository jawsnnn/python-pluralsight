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

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32

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
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value > RefrigeratedShipping.MAX_CELSIUS:
            raise ValueError("Too Hot")
        self._celsius = value

    @property
    def fahrenheit(self):
        return RefrigeratedShipping._c_to_f(self.celsius)


    # This is important. We set the celsius property thereby using the setter validations on that property
    # while using f to c conversion so that the function can take as input fahrenheit values
    # And the fahrenheit getter function ensures that we provide an interface to get f values

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = RefrigeratedShipping._f_to_c(value)
