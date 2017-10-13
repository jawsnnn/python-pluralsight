# Usage of classmethods: Creation of named constructors

class Shipping:

    next_serial = 1337

    # Assume that all shipping containers have the same width and height

    HEIGHT_FT = 10.0
    WIDTH_FT = 5.0

    @classmethod
    def _get_next_serial_num(cls):
        Shipping.next_serial += 1
        return Shipping.next_serial

    @classmethod
    def _get_bic_code(cls, owner_code, serial):
        return owner_code+'U'+str(serial).zfill(6)

    @classmethod
    def create_empty(cls, owner_code, length, *args, **kwargs):
        return cls(owner_code = owner_code, contents = None, length = length, *args, **kwargs)

    @classmethod
    def create_with_list(cls, owner_code, items, length, *args, **kwargs):
        return cls(owner_code = owner_code, contents = list(items), length = length, *args, **kwargs)

    def _get_volume(self):
        return Shipping.HEIGHT_FT * Shipping.WIDTH_FT * self.length

    @property
    def volume_ft(self):
        return self._get_volume()

    # This can be easily overwritten
    def non_static(self):
        print("This is a shipping container")

    def __init__(self, owner_code, contents, length):
        self.owner_code = owner_code
        self.length = length
        self.contents = contents
        # Polymorphism does not work with static methods
        self.bic = self._get_bic_code(owner_code = self.owner_code,
                serial = Shipping._get_next_serial_num())

class RefrigeratedShipping(Shipping):

    MAX_CELSIUS = 4.0

    # This says that the volume of refrigeration equipment is 100
    REFRIGERATED_EQUIP_VOLUME = 100.0

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

    def __init__(self, owner_code, contents, celsius, length):
        super().__init__(owner_code, contents, length)
        self.celsius = celsius

    def _get_celsius(self):
        return self._celsius

    @property
    def celsius(self):
        return self._get_celsius()

    def _set_celsius(self, value):
        if value > RefrigeratedShipping.MAX_CELSIUS:
            raise ValueError("Too Hot!!")
        self._celsius = value

    @celsius.setter
    def celsius(self, value):
        self._set_celsius(value)

    @property
    def fahrenheit(self):
        return RefrigeratedShipping._c_to_f(self.celsius)


    # This is important. We set the celsius property thereby using the setter validations on that property
    # while using f to c conversion so that the function can take as input fahrenheit values
    # And the fahrenheit getter function ensures that we provide an interface to get f values

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = RefrigeratedShipping._f_to_c(value)

    @property
    def volume_ft(self):
        return super()._get_volume() - RefrigeratedShipping.REFRIGERATED_EQUIP_VOLUME 



class HeatedShipping(RefrigeratedShipping):

    MIN_CELSIUS = -20.0
    
    # The ugly override was solved by defining template functions at each level in the hierarchy
    # and overriding those functions instead of explicitly calling fset in the Property object
    # This function only modifies the template function which is called in the Property object

    def _set_celsius(self, value):
        if value < HeatedShipping.MIN_CELSIUS:
            raise ValueError("Too cold")
        return  super()._set_celsius(value)
