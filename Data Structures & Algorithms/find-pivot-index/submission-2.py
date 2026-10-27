class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum = 0

        for i in range(len(nums)):
            rsum = lsum - lsum - nums[i]
            if rsum == lsum:
                return i
            lsum += nums[i]
        
        return -1