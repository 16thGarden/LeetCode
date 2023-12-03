# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if (x < 0):
            negative = True
            x = -x
        
        ans = 0
        while (x > 0):
            ans *= 10
            ans += x % 10
            x //= 10

        rangeLower = -2 ** 31
        rangeUpper = 2 ** 31 - 1

        if (ans > rangeUpper or ans < rangeLower):
            ans = 0
        elif (negative):
            ans = -ans

        return ans