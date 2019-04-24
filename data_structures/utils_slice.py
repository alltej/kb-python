import unittest


class UtilsTest(unittest.TestCase):

    def test_slice(self):
        seq = 'Monty Python'
        self.assertEqual('Pyth', seq[6:10], "Slice 4 elements starting at index 6 and ending at index 9")
        self.assertEqual('Monty', seq[:5], "Omit start to default to start of the sequence")
        self.assertEqual('Python', seq[6:], "Omit end to default to end of the sequence")

    def test_get_every_other_element(self):
        seq = 'Monty Python'
        self.assertEqual('MnyPto', seq[::2], "get every other elemtn")

    def test_reverse_list_or_tuple(self):
        seq = 'Monty Python'
        self.assertEqual(seq[::-1], 'nohtyP ytnoM', "reverses the list/tuple")

if __name__ == '__main__':
    unittest.main()