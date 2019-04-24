import unittest


class TestEnumerate(unittest.TestCase):

    #Get the index of a collection and the value:
    def test_enumerate(self):
        strings = ['foo', 'bar', 'baz']
        for i, string in enumerate(strings):
            print(i, string)


if __name__ == '__main__':
    unittest.main()

# will display the following
# (0, 'foo')
# (1, 'bar')
# (2, 'baz')
