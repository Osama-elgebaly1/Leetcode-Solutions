# Algorithm: Use a stack to track opening brackets and match with closing brackets.
class Solution(object):
    def isValid(s):
        """
            :type s: str
            :rtype: bool
        """
                
        stack = []  # Initialize an empty stack
        hash = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        
        for bracket in s:
            if bracket in hash:  # If it's a closing bracket
                if stack and stack[-1] == hash[bracket]:
                    stack.pop()  # Pop the opening bracket if it matches
                else:
                    return False  # Return False if no match
            else:
                stack.append(bracket)  # If it's an opening bracket, add to stack
        # If stack is empty, return True, otherwise False
        if stack:
            return False
        else:
            return True  # If stack is empty, return True, otherwise False

