import unittest


class TestSorted(unittest.TestCase):

    # Return a new sorted list from the elements of a sequence O(n log n):
    def test_sorted(self):
        seq = sorted([2, 5, 1, 8, 7, 9])
        self.assertEqual([1, 2, 5, 7, 8, 9], seq, "sorted integers")

    def test_sorted_string(self):
        seq = sorted('foo bar baz')
        self.assertEqual([' ', ' ', 'a', 'a', 'b', 'b', 'f', 'o', 'o', 'r', 'z'], seq, "sorted strings")

    # get a sorted list of unique elements by combining sorted and set:
    def test_sort_list_of_unique_elements(self):
        seq = [2, 5, 1, 8, 7, 9, 9, 2, 5, 1, (4, 2), (1, 2), (1, 2)]
        my_set = set(seq)
        sorted_unique = sorted(my_set)
        self.assertEqual([1, 2, 5, 7, 8, 9, (1, 2), (4, 2)], sorted_unique, "sorted unique elements")


if __name__ == '__main__':
    unittest.main()
