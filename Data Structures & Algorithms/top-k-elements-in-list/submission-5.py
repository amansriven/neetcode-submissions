class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        q = []
        for num, count in freq.items():
            heapq.heappush(q, (-count, num))
        res = []

        while q and k > 0:
            num = heapq.heappop(q)[1]
            res.append(num)
            k -= 1

        return res
        