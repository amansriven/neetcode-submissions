class Solution:
    def help(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return -1

    def search(self, nums: List[int], target: int) -> int:
        r = len(nums) - 1
        if nums[0] > nums[r]:
            while nums[0] > nums[r]:
                r -= 1
        search1 = self.help(nums[:r+1], target)
        search2 = self.help(nums[r+1:], target)

        if search1 and search2 == -1:
            return -1
        if search2 == -1:
            return search1
        
        return max(search1, r + 1 + search2)