import unittest
from sorted_set import SortedSet

class TestConstruction(unittest.TestCase):

    def test_with_empty(self):
        s = SortedSet([])

    def test_with_sequence(self):
        s = SortedSet([7,8,4,3])

    def test_with_iterable(self):
        def gen123():
            yield 4
            yield 3
            yield 5
            yield 8
            yield 2
        g = gen123()
        s = SortedSet(g)

    def test_with_duplicates(self):
        s = SortedSet([1, 4, 3, 1, 5, 4])

    def test_with_defauly_empty(self):
        s = SortedSet()

# Protocol 1: Container. Allows checking using in and not in

class TestContainer(unittest.TestCase):

    def setUp(self):
        self.s = SortedSet([1, 5, 6, 9])

    def test_positive_contained(self):
        self.assertTrue(6 in self.s)

    def test_negative_contained(self):
        self.assertFalse(2 in self.s)

    def test_pos_not_contained(self):
        self.assertTrue(8 not in self.s)

    def test_neg_not_contained(self):
        self.assertFalse(5 not in self.s)

class TestSize(unittest.TestCase):

    def test_empty(self):
        s = SortedSet()
        self.assertEqual(len(s) , 0)

    def test_one(self):
        s = SortedSet([9])
        self.assertEqual(len(s) , 1)

    def test_ten(self):
        s = SortedSet(range(10))
        self.assertEqual(len(s) , 10)

    def test_dupes(self):
        s = SortedSet([4, 4, 4])
        self.assertEqual(len(s) , 1)



if __name__ == '__main__':
    unittest.main()


