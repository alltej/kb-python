import unittest


class TestZip(unittest.TestCase):

    # Pair up the elements of sequences to create a list of tuples:
    def test_zip(self):
        seq_1 = [1, 2, 3]
        seq_2 = ['foo', 'bar', 'baz']
        val = zip(seq_1, seq_2)
        self.assertEqual([(1, 'foo'), (2, 'bar'), (3, 'baz')], val, "zipped")

    # Zip takes an arbitrary number of sequences. The number of elements it produces
    # is determined by the shortest sequence:
    def test_zip_shortest_seq(self):
        seq_1 = [1, 2, 3]
        seq_2 = ['foo', 'bar', 'baz']
        seq_3 = [True, False]
        val = zip(seq_1, seq_2, seq_3)
        self.assertEqual([(1, 'foo', True), (2, 'bar', False)], val, "zipped")

    def test_zip_with_enumerate(self):
        seq_1 = [1, 2, 3]
        seq_2 = ['foo', 'bar', 'baz']
        for i, (a, b) in enumerate(zip(seq_1, seq_2)):
            print('%d: %s, %s' % (i, a, b))

        # prints below:
        # 0: 1, foo
        #
        # 1: 2, bar
        #
        # 2: 3, baz

    def test_unzip_seq(self):
        numbers = [(1, 'one'), (2, 'two'), (3, 'three')]
        a, b = zip(*numbers)
        self.assertEqual((1, 2, 3), a, "a")
        self.assertEqual(('one', 'two', 'three'), b, "b")


if __name__ == '__main__':
    unittest.main()
