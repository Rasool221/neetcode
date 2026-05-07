import heapq

# divide input array into 2 heaps
# max of left and min of right should let us calculate median
# odd number of elements: top of largest heap
# even number of elements: top of l + top of r / 2
# inserting should keep the 2 heaps balanced
# [1, 2, 3]
# insert 1: l = [1], r = []
# insert 2: l = [1, 2], r = [] (2 > 1 put in left)
#           l = [1], r = [2] (rebalance heap by popping max, moving to right)
# insert 3: l = [1], r = [2, 3] (3 > 2, put in right)

# [1, 3, 2]
# insert 1: l = [1], r = []
# insert 3: l = [1, 3], r = [] (3 > 1 put in left)
#           l = [1], r = [3] (rebalance heap, pop max, move to right)
# insert 2: l = [1, 2], r = [3] (2 > 1 and 2 < 3, put in left)

# insert should still remain O(lgn) since we're inserting twice in 2 passes
# we have to balance both ways, left and right
class MedianFinder:

    def __init__(self):
       self.l = [] # left heap
       self.r = [] # right heap

    def addNum(self, num: int) -> None:
        l = self.l[0] if len(self.l) > 0 else float('-inf')
        r = self.r[0] if len(self.r) > 0 else float('inf')

        # print(f"{num=}")

        if num <= l:
            heapq.heappush_max(self.l, num)
        elif num >= l and num <= r:
            heapq.heappush_max(self.l, num)
        elif num >= l and num >= r:
            heapq.heappush(self.r, num)

        l_len = len(self.l)
        r_len = len(self.r)

        # balancing by popping from left
        # insert into right
        if abs(l_len - r_len) > 1:
            if l_len > r_len: 
                l_val = heapq.heappop_max(self.l)
                heapq.heappush(self.r, l_val)
            else:
                r_val = heapq.heappop(self.r)
                heapq.heappush_max(self.l, r_val)

    def findMedian(self) -> float:
        c = len(self.l) + len(self.r)
        if c % 2 == 0:
            l = self.l[0]
            r = self.r[0]
            print(f"{l=}, {r=}")
            return (l + r) / 2

        if len(self.l) > len(self.r):
            return float(self.l[0])
        else:
            return float(self.r[0])

        