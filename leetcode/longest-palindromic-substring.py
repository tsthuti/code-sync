class Solution(object):
    def longestPalindrome(self, s):

        if len(s) <= 1:
            return s

        start = 0
        end = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # return the valid palindrome boundaries
            return left + 1, right - 1

        for i in range(len(s)):
            # odd length palindrome (ex: "aba")
            left1, right1 = expand(i, i)

            # even length palindrome (ex: "abba")
            left2, right2 = expand(i, i + 1)

            if right1 - left1 > end - start:
                start, end = left1, right1

            if right2 - left2 > end - start:
                start, end = left2, right2

        return s[start:end+1]