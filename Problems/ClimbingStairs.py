# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

dp = [None] * 46
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 5
dp[5] = 8
dp[6] = 13
dp[7] = 21
dp[8] = 34
dp[9] = 55
dp[10] = 89
dp[11] = 144
dp[12] = 233
dp[13] = 377
dp[14] = 610
dp[15] = 987
dp[16] = 1597
dp[17] = 2584
dp[18] = 4181
dp[19] = 6765
dp[20] = 10946
dp[21] = 17711
dp[22] = 28657
dp[23] = 46368
dp[24] = 75025
dp[25] = 121393
dp[26] = 196418
dp[27] = 317811
dp[28] = 514229
dp[29] = 832040
dp[30] = 1346269
dp[31] = 2178309
dp[32] = 3524578
dp[33] = 5702887
dp[34] = 9227465
dp[35] = 14930352
dp[36] = 24157817
dp[37] = 39088169
dp[38] = 63245986
dp[39] = 102334155
dp[40] = 165580141
dp[41] = 267914296
dp[42] = 433494437
dp[43] = 701408733
dp[44] = 1134903170
dp[45] = 1836311903

class Solution:
    def climbStairs(self, n: int) -> int:    
        return dp[n]