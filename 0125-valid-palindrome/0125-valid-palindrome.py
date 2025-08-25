class Solution(object):
    def isPalindrome(self, s):
        start, end = 0, len(s) - 1

        while start < end:

            if not (48 <= ord(s[start]) <= 57 or 65 <= ord(s[start]) <= 90 or 97 <= ord(s[start]) <= 122):
                start += 1
                continue

            if not (48 <= ord(s[end]) <= 57 or 65 <= ord(s[end]) <= 90 or 97 <= ord(s[end]) <= 122):
                end -= 1
                continue

            a, b = ord(s[start]), ord(s[end])

            if a != b and not (65 <= a <= 90 and a + 32 == b) and not (97 <= a <= 122 and a - 32 == b):
                return False

            start += 1
            end -= 1

        return True