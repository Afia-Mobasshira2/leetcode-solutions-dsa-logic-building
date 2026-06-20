class Solution(object):
    def isValid(self, s):
        # 1. Create an empty list to act as our stack
        stack = []
        
        # 2. Loop through each character in the string
        for char in s:
            # If it's an opening bracket, push it onto the stack
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
                
            # If it's a closing bracket
            else:
                # If the stack is empty, there's no opening bracket to match it!
                if len(stack) == 0:
                    return False
                    
                # Pop the top bracket off the stack
                top = stack.pop()
                
                # Check if they mismatch
                if char == ')' and top != '(': return False
                if char == ']' and top != '[': return False
                if char == '}' and top != '{': return False
                
        # If the stack is completely empty at the end, everything matched perfectly!
        return len(stack) == 0