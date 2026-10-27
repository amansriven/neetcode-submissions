class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxA = -float('inf')

        while l < r:
            currA = min(heights[l], heights[r]) * (r - l)
            maxA = max(currA, maxA)

            if heights[r-1] > heights[l+1]:
                r -= 1
            else:
                l += 1
        
        return maxA