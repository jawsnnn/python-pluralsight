class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # a representation should have at least the class name, and the values the objects holds
    # Some say that a repr should be syntactically accurate enought to recreate the object (as here)
    # But at the very least it should be helpful to a person debugging the program by providing detailed infomration
    # Suitable for logging as has more information, not necessarily reader friendly
    # Developers use repr, clients use str

    def __repr__(self):
        return "Point2D(x={}, y={})".format(self.x, self.y)


    # Intedend to provide human friendly contents
    # Can be used in presentation code to expose values of object

    def __str__(self):
        return "The X and Y coordinates of this point are ({},{})".format(self.x, self.y)


    # Format function is called when a formatted string is used with the object
    # the f argument provides and optional formatting flag that can be implemented
    # Here when the formatter is called with {:r}, the x and y coordinates will be reversed
    # Some other default flags are:
    #   {!r} for printing repr()
    #   {!s} for priting str()
    # If __format__ is not overridden it just calls str()

    def __format__(self, f):
        if f == 'r':
            return ("Formatted point (reversed): {}, {}".format(self.y, self.x))
        else:
            return ("Formatted point: {}, {}".format(self.x, self.y))
