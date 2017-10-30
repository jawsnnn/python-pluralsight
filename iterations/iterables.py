# Iterables are objects that implement:
#   1. __init__() function and return self or another iterable
#   2. __next__() function
#   3. Raise StopIteration when no values are avialable

class DummyIterator:
    def __init__(self):
        self.counter = 0
        self.data = [1, 2, 3, 4, 5]

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= len(self.data):
            raise StopIteration
        else:
            rslt=self.data[self.counter]
            self.counter += 1
            return rslt

# This object can be looped over: for x in DummyIterator: print x
# OR next can be called on it: x = DummyIterator(); next(x); next(x)....

# An iterable is simply an object that implements dunder iter. thats it
# An iteratort is an object that implements the iterable protocol AND respond to the next() function

# dunder iter is called on an iterable to create and iterator
# dunder next is called on an iterator to retrieve its next value
# iterables do not have next?? why?

# Alternative protocol for iterables

# Implement __getitem__() with index

class AltIterator:
    def __init__(self):
        self.data = [1,2,3,4,5]

    def __getitem__(self, idx):
        return self.data[idx]


# Extended iterators are created by calling the iter function with two args
# The first arg is a callable which returns a single value with zero args provided
# The second arg is a sentinel value which is compared to callable's return
# Iteration stops only when callable returns the sentinel value

class ExtIterator:

    def __init__(self):
        self.limit=10
        self.counter=0
    
    def increment(self):
        self.counter+=1
        return self.counter

"""
This is called by:
    >>> from iterables import ExtIterator
    >>> x = ExtIterator()
    >>> for i in iter(x.increment, x.limit):
        ...     print(i)
        ...
        1
        2
        3
        4
        5
        6
        7
        8
        9

This is useful for creating infinite sequences. YOu can create one by creating an iter with None or improbable return value
"""
