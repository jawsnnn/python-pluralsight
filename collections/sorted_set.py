class SortedSet:

    # Adding the set constructor to remove dupes
    def __init__(self, *args):
        self._items = sorted(set(*args)) if args else []

    # Implement the container protocol

    def __contains__(self, item):
        return item in self._items

    # Implement the size protocol

    def __len__(self):
        return len(self._items)
