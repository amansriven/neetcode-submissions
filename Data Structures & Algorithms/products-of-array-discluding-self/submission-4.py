class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lprod = 1
        left = []
        for x in nums:
            left.append(lprod)
            lprod *= x
        
        rprod = 1
        right = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            right[i] = rprod
            rprod *= nums[i]
        res = []
        for i in range(len(nums)):
            res.append(right[i] * left[i])
        return res
            
