class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        strnum = "".join(str(num) for num in digits)

        incr = int(strnum)+1
        newstr=[int(d) for d in str(incr)]
        
        return newstr