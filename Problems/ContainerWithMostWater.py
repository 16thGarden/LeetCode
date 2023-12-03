# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(height) - 1

        while(left != right):
            h = min(height[left], height[right])
            l = right - left

            area = h * l
            
            if maxArea < area:
                maxArea = area
            
            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1
                        
        return maxArea