# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        o = x
        r = 0

        while (o > 0):
            r *= 10
            r += o % 10
            o //= 10
        
        return r == x