# i think we run 2 passes over the intervals list, one to insert it where it should be,
# and another to merge if anything needs to be merged
# actually, 3 pass solution, where the last pass is to clean up the intervals array
# by removing overlapping intervals
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insert_index = 0
        c, d = newInterval

        # first pass, grab an index where to insert it at
        for i in range(len(intervals)):
            a, b = intervals[i]

            if c >= a and b <= d:
                insert_index = i + 1

        intervals.insert(insert_index, newInterval)

        remove_indexes = []

        # second pass, merge intervals
        for i in range(1, len(intervals)):
            a, b = intervals[i]
            e, f = intervals[i - 1]

            # print(f"before {i=} {intervals=}")

            # intervals overlap if b equal to or in between prev intervals numbers
            if f >= a and f <= b or (f >= a and f >= b):
                intervals[i] = [min(e, a), max(b, f)] # override cur element to new interval
                remove_indexes.append(i - 1) # mark the index to remove

            # print(f"after {i=} {intervals=} {remove_indexes=}")

        # remove indexes we marked earlier from intervals
        c = 0
        for remove in remove_indexes:
            intervals.pop(remove - c)
            c += 1
        
        return intervals