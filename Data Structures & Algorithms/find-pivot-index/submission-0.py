class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = []
        lsum = 0

        for x in nums:
            left.append(lsum)
            lsum += x
        
        rsum = 0
        for i in range(len(nums)-1, -1, -1):
            if rsum == left[i]:
                return i
            rsum += nums[i]
        
        return -1