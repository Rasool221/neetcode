import math

# piles = [1,4,2,3], h = 9 (amount of hours), k = bananas per hours
# what's the minimum k we can have 
# we know that k <= max(piles) because if we can eat largest pile in one hour, we can eat all in less
# we can also calculate total amount of hours it takes to eat bananes x using total_time = ceil(x/k)
# if total_time <= h, we know that its viable. then we just find the min total_time.
# this means we can build a monotonically increasing answer space of k, from 1..max(piles),
# and test if ceil(max(piles)/k) <= h, if it is, we note a global_min
# we can check efficiently using binary search

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)

        lower = 1
        upper = max_pile
        gmin = float('inf')

        while lower <= upper:
            mid = (upper + lower) // 2
            
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile/mid)

            if total_time <= h:
                gmin = min(gmin, mid)
                upper = mid - 1
            if total_time > h:
                lower = mid + 1 

        return gmin