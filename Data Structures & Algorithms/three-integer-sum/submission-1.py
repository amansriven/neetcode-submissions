class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if curr == 0:
                    res.append([nums[l],nums[i],nums[r]]) 
                    l, r = l + 1, r - 1
                if curr > 0:
                    r -= 1
                if curr < 0:
                    l += 1
        return res

# -2,0,0,2,2