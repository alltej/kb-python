# %load test_permutation_solution.py
# from nose.tools import assert_equal
from nose.tools import assert_equal

from permutations import Permutations


class TestPermutation(object):

    def test_permutation(self, func):
        assert_equal(func(None, 'foo'), False)
        assert_equal(func('', 'foo'), False)
        assert_equal(func('Nib', 'bin'), False)
        assert_equal(func('act', 'cat'), True)
        assert_equal(func('a ct', 'ca t'), True)
        print('Success: test_permutation')


def main():
    test = TestPermutation()
    permutations = Permutations()
    test.test_permutation(permutations.is_permutation)

if __name__ == '__main__':
    main()