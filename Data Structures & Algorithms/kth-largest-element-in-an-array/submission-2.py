import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        heapq.heapify(h)

        for n in nums:
            if len(h) >= k:
                heapq.heappop(h)
                
            heapq.heappush(h, n)

        return h[0]
        