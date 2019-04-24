import unittest
import bisect


# The bisect module does not check whether the list is sorted, as this check would be expensive O(n). Using bisect on
# an unsorted list will not result in an error but could lead to incorrect results.
class TestBisect(unittest.TestCase):

    # Find the location where an element should be inserted to keep the list sorted:
    def test_bisect(self):
        seq = [1, 2, 2, 3, 5, 13]
        loc = bisect.bisect(seq, 8)
        self.assertEqual(5, loc, "index to insert 8 to keep the list sorted")

    # Insert an element into a location to keep the list sorted:
    def test_insert(self):
        seq = [1, 2, 2, 3, 5, 13]
        bisect.insort(seq, 8)
        self.assertEqual([1, 2, 2, 3, 5, 8, 13], seq, "")

if __name__ == '__main__':
    unittest.main()
