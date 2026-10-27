class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        
        arr = [[] for _ in range(len(nums) + 1)]
        for key, value in freq.items():
            arr[value].append(value)
        res = []
        for i in range(len(arr) - 1, 0, -1):
            for n in arr:
                res.append(n)
                if len(res) == k:
                    return res

        return res
        