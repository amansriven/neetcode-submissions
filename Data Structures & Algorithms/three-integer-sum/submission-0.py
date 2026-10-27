class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        seen = set()
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            if nums[i] in seen:
                continue
            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if curr == 0:
                    res.append([nums[l],nums[i],nums[r]])
                    seen.add((i,l,r))
                    l += 1
                    r -= 1
                if curr > 0:
                    r -= 1
                if curr < 0:
                    l += 1
            seen.add(nums[i])
        return res