def matching(s):
    stack = []
    for char in s:
        if char=="(" or char=="[" or char=="{":
            stack.append(char)
        elif char==")" and stack and stack[-1]=="(":
            stack.pop()
        elif char=="]" and stack and stack[-1]=="[":
            stack.pop()
        elif char=="}" and stack and stack[-1]=="{":
            stack.pop()
        
    return len(stack) == 0
