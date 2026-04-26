import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = nums
        heapq.heapify(self.h)
        self.k = k

        while len(self.h) > k:
            heapq.heappop(self.h)

    def add(self, val: int) -> int:
        # only add to heap if val > kth largest
        if len(self.h) >= self.k and val <= self.h[0]:
            return self.h[0]

        # maintaining a heap window of size k
        if len(self.h) == self.k:
            heapq.heappop(self.h)

        heapq.heappush(self.h, val)

        # return smallest value, which is kth largest
        return self.h[0]
