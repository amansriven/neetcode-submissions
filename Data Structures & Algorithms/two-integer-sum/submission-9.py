class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in idx:
                return [idx[comp], i]
            idx[nums[i]] = i
        return []