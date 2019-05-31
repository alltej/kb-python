from nose.tools import assert_equal

import working_hours


class TestWorkingHours(object):

    def is_working_hours_func(self, func):
        assert_equal(func(9), True)
        assert_equal(func(11), True)
        assert_equal(func(13), True)
        assert_equal(func(15), True)
        assert_equal(func(18), True)

        assert_equal(func(8), False)
        assert_equal(func(20), False)
        assert_equal(func(23), False)
        assert_equal(func(0), False)
        assert_equal(func(1), False)
        assert_equal(func(3), False)
        assert_equal(func(5), False)
        print('Success: test_working_hours')

    def is_non_working_hours_func(self, func):
        assert_equal(func(9), False)
        assert_equal(func(11), False)
        assert_equal(func(13), False)
        assert_equal(func(15), False)
        assert_equal(func(18), False)

        assert_equal(func(0), True)
        assert_equal(func(1), True)
        assert_equal(func(3), True)
        assert_equal(func(5), True)
        assert_equal(func(8), True)
        assert_equal(func(20), True)
        assert_equal(func(23), True)
        print('Success: test_non_working_hours')


def main():
    test = TestWorkingHours()
    try:
        wh = working_hours.WorkingHours()
        test.is_working_hours_func(wh.is_working_hours)
        test.is_non_working_hours_func(wh.is_non_working_hours)
    except NameError:
        pass


if __name__ == '__main__':
    main()
