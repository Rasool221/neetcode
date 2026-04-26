import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        heapq.heapify(h)

        for n in nums:
            top = h[0] if len(h) > 0 else float('inf')
            if len(h) >= k and n <= top:
                continue
            
            if len(h) == k:
                heapq.heappop(h)

            heapq.heappush(h, n)

        return h[0]
        