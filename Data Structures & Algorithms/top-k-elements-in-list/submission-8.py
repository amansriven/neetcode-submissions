class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        count = [[] for _ in range(len(nums) + 1)]
        
        for key, val in freq.items():
            count[val].append(key)
        
        res = []
        for i in range(len(nums), -1, -1):
            for x in count[i]:
                res.append(x)
                if len(res) == k:
                    return res