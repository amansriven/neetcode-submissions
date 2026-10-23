class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lprod = 1
        res = []
        for x in nums:
            res.append(lprod)
            lprod *= x
        
        rprod = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * rprod
            rprod *= nums[i]
    
        return res
