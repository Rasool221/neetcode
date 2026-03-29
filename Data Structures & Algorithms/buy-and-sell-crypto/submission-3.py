class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        gmin = float('inf')
        gmax = float('-inf')
        for i in range(len(prices)):
            n = prices[i]

            gmin = min(gmin, n)

            if n > gmin:
                gmax = max(gmax, n - gmin)
            
        return max(gmax, 0)
