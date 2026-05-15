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
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        # need the first for the first element at least, so rooms starts with 1
        rooms = 1
        last_end = intervals[0].end

        for i in range(1, len(intervals)):
            cur = intervals[i]

            if last_end > cur.start:
                rooms += 1
                last_end = min(last_end, cur.end)

        return rooms