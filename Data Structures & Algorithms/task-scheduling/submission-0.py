# mathematically:
# the number of cycles has to be at least the amount of repeating chars + n
# [X, X, Y, Y] the amount of repeating chars is 2, 
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for i in range(len(tasks)):
            c = tasks[i]
            freq[c] = freq.get(c, 0) + 1

        amt_most_common = max(freq.values())
        print(amt_most_common)
        return 0
        