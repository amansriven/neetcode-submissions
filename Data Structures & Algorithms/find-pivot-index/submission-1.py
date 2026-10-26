class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = []
        lsum = 0

        for x in nums:
            left.append(lsum)
            lsum += x
        
        for i in range(len(nums)):
            rsum = lsum - left[i] - nums[i]
            if rsum == left[i]:
                return i
        
        return -1