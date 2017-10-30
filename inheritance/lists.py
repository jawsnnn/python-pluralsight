class SimpleList:

    def __init__(self, items):
        self._items = list(items)

    def __getitem__(self, idx):
        return self._items[idx]

    def add(self, x):
        self._items.append(x)

    def sort(self):
        self._items.sort()

    def __repr__(self):
        list_str = str(self._items[0])
        for x in self._items[1:]:
            list_str=list_str+','+str(x)
        return list_str


class SortedList(SimpleList):
    def __init__(self, items):
        super().__init__(items)
        self.sort()

    def add(self, x):
        super().add(x)
        self.sort()


class IntList(SimpleList):
    def __init__(self, items):
        for x in items:
            if not isinstance(x, int):
                raise TypeError("This list only accepts Int")
        super().__init__(items)


    def add(self, x):
        if not isinstance(x, int):
            raise TypeError("This list only accepts Int")
        super().add(x)

class IntSortedList(IntList, SortedList):
    def __repr__(self):
        return "IntSortedList({!r})".format(list(self))
