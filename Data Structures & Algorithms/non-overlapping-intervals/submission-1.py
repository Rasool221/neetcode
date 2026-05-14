# first we sort by the first element of the interval
# then we simply count the amount of overlapping ones
# well that wont return the minimum always, so we can revisit that later, but 
# i want to get the shell of the solution set up first
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by first element so we can count by looking
        # ahead
        intervals.sort(key=lambda x: x[0]) 

        amt_to_remove = 0
        
        # count overlapping intervals
        # we dont need to look at the last element
        for i in range(len(intervals) - 1): 
            a, b = intervals[i]
            c, d = intervals[i + 1]

            # 2 checks, do intervals overlap?
            # and are intervals identical?
            if (b > c and b < d) or (a == c and b == d):
                amt_to_remove += 1
            
        return amt_to_remove