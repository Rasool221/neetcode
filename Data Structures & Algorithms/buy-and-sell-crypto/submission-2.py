# [10,1,5,6,7,1]
# l = 10, r = 1, l > r so l += 1
# l = 1, r = 1, r == l so l -= 1
# we know that we need to have a smaller number on left, and larger on the right
# global max counter starts at = 0, when diff of both l - r <= 1, we break

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = 0
        gmax = 0
    
        while l <= len(prices) - 1:
            ln = prices[l]
            rn = prices[r]
            # print(ln, rn)

            if ln > rn:
                l += 1
                r = l
            else:
                gmax = max(gmax, rn - ln)

            if r == len(prices) - 1:
                l += 1
                r = l
            else:
                r += 1

        return gmax
