import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        # print(f"{self.h=}, {self.k=}")
        return self.h[max(len(self.h)-self.k, 0)]
