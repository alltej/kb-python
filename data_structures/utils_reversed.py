import unittest


class TestReversed(unittest.TestCase):

    def test_reversed(self):
        seq = [2, 5, 1, 8, 7, 9, 9, 2, 5, 1, (4, 2), (1, 2), (1, 2)]
        reversed_seq = list(reversed(seq))
        self.assertEqual([(1, 2), (1, 2), (4, 2), 1, 5, 2, 9, 9, 7, 8, 1, 5, 2], reversed_seq, "reversed")


if __name__ == '__main__':
    unittest.main()
