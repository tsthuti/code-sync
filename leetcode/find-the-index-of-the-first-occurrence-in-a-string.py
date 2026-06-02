class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        idx = []
        start = haystack.find(needle)
        
        if start != -1:
            idx.append(start)

        return idx[0] if idx else -1