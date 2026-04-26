import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = stones
        heapq.heapify_max(h)

        while len(h) > 1:
            x = h[0]
            y = h[1]

            heapq.heappop(h)
            heapq.heappop(h)

            if x < y:
                heapq.heappush(h, y - x)
            elif x > y:
                heapq.heappush(h, x - y)

        return 0 if len(h) == 0 else h[0]