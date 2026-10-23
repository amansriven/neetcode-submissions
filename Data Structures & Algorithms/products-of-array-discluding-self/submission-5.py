class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lprod = 1
        left = []
        for x in nums:
            left.append(lprod)
            lprod *= x
        
        rprod = 1
        res = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            res[i] = rprod * left[i]
            rprod *= nums[i]
    
        return res
            
