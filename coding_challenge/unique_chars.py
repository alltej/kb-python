
class UniqueCharsSet(object):

    @staticmethod
    def has_unique_chars(string):
        if string is None:
            return False
        return len(set(string)) == len(string)


# class TestUniqueChars(unittest.TestCase):
#
#     def test_unique_chars(self):
#         unique_chars_set = UniqueCharsSet()
#         self.assertEqual(unique_chars_set.has_unique_chars(None), False, "false")
#         self.assertEqual(unique_chars_set.has_unique_chars(''), True, "true")
#         self.assertEqual(unique_chars_set.has_unique_chars("abcdefga"), False, "true")
#
#
# if __name__ == '__main__':
#     unittest.main()
