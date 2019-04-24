import unittest


# In Python 2.x, range returns a list, but in Python 3.x range returns an immutable sequence, of type range
class TestRange(unittest.TestCase):

    def test_generate_integers(self):
        seq = range(10)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], list(seq), "list of integers 0 to 9")

    def test_start_stop_step_args(self):
        seq = range(0, 20, 3)
        self.assertEqual([0, 3, 6, 9, 12, 15, 18], list(seq), "list of integers from 0 to 20 at intervals/steps of 3")

    def test_iterate_by_index(self):
        seq = [1, 2, 3]
        for i in range(len(seq)):
            val = seq[i]
            print(val)

    # For longer ranges, xrange is recommended and is available in Python 3 as range. It returns an iterator that
    # generates integers one by one rather than all at once and storing them in a large list.
    def test_xrange(self):
        sum = 0
        for i in range(100000):
            if i % 2 == 0:
                sum += 1
        self.assertEqual(50000, sum, "should be half of number(100000)")


if __name__ == '__main__':
    unittest.main()
