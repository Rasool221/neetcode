# first we sort by the first element of the interval
# then we simply count the amount of overlapping ones
# well that wont return the minimum always, so we can revisit that later, but 
# i want to get the shell of the solution set up first

# so yeah as i predicted we're not getting the min amount, just 
# how many overlapping there are.

# in this test case for example: intervals=[[0,2],[1,3],[2,4],[3,5],[4,6]]
# my og solution produces 4 while we should be producing 2, which is the minimum

# in order to do this, we need to look behind not ahead because
# we're going to build a running min of ending intervals with the 
# previous so that we can track the least amount of overalapping intervals to remove
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by first element so we can count by looking
        # ahead
        intervals.sort(key=lambda x: x[0]) 

        if len(intervals) == 0:
            return 0

        amt_to_remove = 0
        last_end = intervals[0][1]
        
        # counting min number of overlapping intervals to
        # remove
        # we dont need to look at first element
        for i in range(1, len(intervals)): 
            a, b = intervals[i]

            # if we're overlapping,
            # set new last end as min of cur end and last end,
            # this ensures that we remove as little intervals as possible
            # by picking smaller spans
            # if we're not overlapping, update last end to cur end
            # so we have a fresh window
            if a < last_end:
                last_end = min(b, last_end)
                amt_to_remove += 1
            else:
                last_end = b
            
        return amt_to_remove