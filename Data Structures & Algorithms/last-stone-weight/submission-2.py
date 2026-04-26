import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = stones
        heapq.heapify_max(h)

        while len(h) > 1:
            x = heapq.heappop_max(h)
            y = heapq.heappop_max(h)

            if x < y:
                heapq.heappush_max(h, y - x)
            elif x > y:
                heapq.heappush_max(h, x - y)
            
        return 0 if len(h) == 0 else h[0]