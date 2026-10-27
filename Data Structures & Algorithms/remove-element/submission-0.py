class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        q = deque()
        k = 0

        for i in range(len(nums)):
            if nums[i] == val:
                q.append(i)
                k += 1
            elif q:
                j = q.popleft()
                nums[j] = nums[i]
                nums[i] = val
                q.append(i)
        return len(nums) - k


