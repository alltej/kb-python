from nose.tools import assert_equal

import unique_chars


class TestUniqueChars(object):

    def test_unique_chars(self, func):
        assert_equal(func(None), False)
        assert_equal(func(''), True)
        assert_equal(func('foo'), False)
        assert_equal(func('bar'), True)
        assert_equal(func('hello'), False)
        assert_equal(func('hello'), True)
        print('Success: test_unique_chars')


def main():
    test = TestUniqueChars()
    try:
        unique_chars_set = unique_chars.UniqueCharsSet()
        test.test_unique_chars(unique_chars_set.has_unique_chars)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()
