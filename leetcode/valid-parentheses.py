class Solution:
    def isValid(self, s: str) -> bool:
        # if not even, we know that the brackets are missing their closing brace
        if ((len(s)%2)!=0):
            return False
        elif (len(s)<=1):
            return False
        
        pars = {
            "[": "]",
            "{": "}",
            "(": ")"
        }

        opener=0
        closer=0

        # treating this array like a stack to push opening brackets onto until they are closed
        arr=[]

        # loop over each char in s
        for char in s:
            # if its an opening brace, push to 'stack'
            if char=="(" or char=="[" or char=="{":
                arr.append(char)
                opener+=1
            # if closing brace
            if char==")" or char=="]" or char=="}":
                # arr not empty && there is a matching opening brace, pop it
                # check dict and see if it matches bc stack ctn only the OPEN braces        
                closer+=1
                if arr and (pars[arr[-1]] == char):
                    arr.pop()
                else:
                    # otherwise, no matching pair and we return false
                    return False

        if(opener!=closer):
            return False

        return True