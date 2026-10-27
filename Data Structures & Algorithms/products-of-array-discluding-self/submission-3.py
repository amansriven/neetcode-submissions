class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        for x in nums:
            prod *= x
        res = []
        for x in nums:
            res.append(prod//x)
        return res