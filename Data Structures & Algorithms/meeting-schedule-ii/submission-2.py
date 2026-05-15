"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# ok so we need to count the min of rooms we need to schedule
# in other words, remove the min number of overlapping intervals, return amount
# since its a problem i just did yesterday, it is a greedy minimization problem
# where we keep track of "last end" time variable iterate through the list (starting with 1st element):
#   if last end overlaps in current interval, set last end as min of cur end and last end, effectively removing the overlapping interval, and keeping window small
#   if last end doesnt overlap, set cur end time to last end
# i think this will work because it is the same problem just rephrased? im a bit confused, i obviously can be wrong

# okay so the above solutions passes for like half test cases but its obviously not the right call
# i think i need to track the max amount of concurrent meetings happening at once
# instead of trying to eliminate overkapping rooms

# first test case [(0,40), (5,10), (15,20)]
# |-----------------------------------------|
# 0  |----|      |----|                     40
#    5    10     15   20

# from the above drawing, we need 2 rooms max since only 2 intervals overlap at a given time
# i can do this by keeping track of meeting end times ive seen so far
# check current interval end time against the smallest end time we see so far
# if smallest time we see so far overlaps with current interval, we need another room 
# otherwise, we can re-use a room (not add another room)
# i can use a min heap, and when we hit the first condition, we would add a new room and add to min heap
# if it doesnt overlap, we pop from min heap and add current end time
# that should keep end time fresh for the next comparison for good overlap checks

# 

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        if len(intervals) == 1:
            return 1

        # sort so we can iterate in meeting time ascending order
        intervals.sort(key=lambda x: x.start)

        # need the first for the first element at least, so rooms starts with 1
        rooms = 0

        # adding first meeting to heap
        h = []
        heapq.heappush(h, intervals[0].end)

        # iterating from second element, with the logic above
        for i in range(1, len(intervals)):
            cur = intervals[i]
            
            min_end = h[0]

            # if min end time doesnt overlap with current end time
            # we pop and add current meeting
            # "re-using an existing room"
            if min_end <= cur.start:
                heapq.heappop(h)

            # add current interval to keep to uphold the logic
            heapq.heappush(h, cur.end)

            # keeping track of max amount of rooms we needed
            rooms = max(rooms, len(h))
            
        return rooms