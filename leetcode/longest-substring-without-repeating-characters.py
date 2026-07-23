class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        seen = set()
        best = 0

        for right, c in enumerate(s):
            while c in seen:
                seen.remove(s[left])
                left += 1

            seen.add(c)
            best = max(best, right - left + 1)
        
        return best