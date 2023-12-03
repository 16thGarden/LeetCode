# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if (c == '(' or c == "{" or c == "["):
                stack.append(c)
            else:
                if (not stack):
                    return False
                
                popped = stack.pop()
                
                if (popped == '(' and c != ')'):
                    return False
                if (popped == '{' and c != '}'):
                    return False
                if (popped == '[' and c != ']'):
                    return False
        
        return not stack