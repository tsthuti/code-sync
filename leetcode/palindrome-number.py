class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num_list =[]
        pal_len = len(str(x))

        for ind, num in enumerate(str(x)):
            num_list.append(num)

        rev_list = num_list[::-1]

        i=0

        for dig in num_list:
            if dig!=(rev_list[i]):
                return False
            else: 
                i+=1

        return True