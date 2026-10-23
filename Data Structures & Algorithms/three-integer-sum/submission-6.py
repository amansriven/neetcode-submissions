class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # -4, -1, -1, 0, 1, 2
        res = []

        for i in range(len(nums)):
            l, r = i+1, len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue
            

            while l < r:

                curr = nums[l] + nums[i] + nums[r]

                if curr == 0:
                    res.append([nums[l], nums[i], nums[r]])
                if curr > 0:
                    r -= 1
                else:
                    l += 1
                
                while l < r and l > 0 and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and r < len(nums) - 1 and nums[r] == nums[r+1]:
                    r -= 1
            

        return res