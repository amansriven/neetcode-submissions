class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in idx:
                if idx[comp] > i:
                    return [i, idx[comp]]
                return [idx[comp], i]
            else:
                idx[nums[i]] = i
        return []