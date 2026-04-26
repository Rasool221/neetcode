import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = nums
        heapq.heapify(h)

        while len(h) > k:
            heapq.heappop(h)

        return h[0]
        