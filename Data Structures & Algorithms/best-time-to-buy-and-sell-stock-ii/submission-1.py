class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxp = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                while r < len(prices) - 1 and prices[r] < prices[r + 1]:
                    r += 1
                maxp += prices[r] - prices[l]
            
            l, r = r, r + 1
        
        return maxp