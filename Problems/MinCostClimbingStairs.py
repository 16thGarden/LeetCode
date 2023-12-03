# 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/

optimalCosts = [None] * 1000
class Solution:
    def minCostClimbingStairs(self, costs):
        for i in range(len(optimalCosts)):
            optimalCosts[i] = None
        
        lcost = len(costs)
        optimalCosts[lcost - 1] = costs[lcost - 1]
        optimalCosts[lcost - 2] = costs[lcost - 2]
        zeroStep = self.rec(0, costs)
        oneStep = self.rec(1, costs)

        return zeroStep if zeroStep < oneStep else oneStep

    def rec(self, n, costs) -> int:
        if (optimalCosts[n] is None):            
            oneStep = costs[n] + self.rec(n + 1, costs)
            twoStep = costs[n] + self.rec(n + 2, costs)
            optimalCosts[n] = oneStep if oneStep < twoStep else twoStep
        
        return optimalCosts[n]