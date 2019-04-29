class ReverseString(object):

    def reverse(self, chars):
        # TODO: Implement me
        if chars:
            size = len(chars)
            for i in range(size // 2):
                chars[i], chars[size - 1 - i] = \
                    chars[size - 1 - i], chars[i]
        return chars

    def reverse_string_alt(self, string):
        if string:
            return string[::-1]
        return string

    def reverse_string_alt2(self, string):
        if string:
            return ''.join(reversed(string))
        return string