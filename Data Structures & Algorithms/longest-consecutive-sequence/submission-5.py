class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for x in numset:
            if x-1 not in numset:
                curr = 1
                nxt = x+1

                while nxt in numset:
                    curr += 1
                    nxt += 1
                
                longest = max(longest, curr)

        return longest