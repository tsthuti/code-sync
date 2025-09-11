class Solution:
    def isPalindrome(self, x: int) -> bool:
        i=0

        # cast num to str and perform basic string comparison
        num = str(x)
        rev_num=num[::-1]
        
        if(num == rev_num): 
            return True
        return False