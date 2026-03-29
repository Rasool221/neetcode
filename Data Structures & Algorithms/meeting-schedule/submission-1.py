"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True

        # sort by end time
        intervals.sort(key=lambda interval: interval.end)

        last_interval = intervals[0].end
        for interval in intervals[1:]:
            if interval.start < last_interval:
                return False

            last_interval = interval.end

        return True