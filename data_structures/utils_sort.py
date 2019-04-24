import unittest

class TestSort(unittest.TestCase):

    # Sort in-place O(n log n)
    def test_sort(self):
        seq = [1, 5, 3, 9, 7, 6]
        seq.sort()
        self.assertEqual([1, 3, 5, 6, 7, 9], seq, "should be sorted")

    def test_sort_by_len(self):
        seq = ['the', 'quick', 'brown', 'fox', 'jumps', 'over']
        seq.sort(key=len)
        self.assertEqual(['the', 'fox', 'over', 'quick', 'brown', 'jumps'], seq, "sorted by len of strings")


if __name__ == '__main__':
    unittest.main()
