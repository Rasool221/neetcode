# i think we run 2 passes over the intervals list, one to insert it where it should be,
# and another to merge if anything needs to be merged
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insert_index = 0
        c, d = newInterval

        # first pass, grab an index where to insert it at
        for i in range(len(intervals)):
            a, b = intervals[i]

            if c >= a and b <= d:
                insert_index = i

        intervals.insert(insert_index+1, newInterval)

        remove_indexes = []

        # second pass, merge intervals
        for i in range(len(intervals)):
            a, b = intervals[i]
            e, f = intervals[i - 1]

            # intervals overlap if b equal to or in between prev intervals numbers
            if f >= a and f <= b:
                intervals[i] = [e, b] # override cur element to new interval
                remove_indexes.append(i - 1) # mark the index to remove

        # remove indexes we marked earlier from intervals
        c = 0
        for remove in remove_indexes:
            intervals.pop(remove - c)
            c += 1
        
        return intervals