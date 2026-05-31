class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.rstrip().split(' ')
        slen = len(s)
        
        return len(s[slen-1])