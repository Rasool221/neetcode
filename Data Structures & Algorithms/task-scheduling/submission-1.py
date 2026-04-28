# mathematically:
# the number of cycles has to be at least the amount of repeating chars + n
# [X, X, Y, Y] the amount of repeating chars is 2, 
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        most_common_amt = 0
        for i in range(len(tasks)):
            c = tasks[i]
            freq[c] = freq.get(c, 0) + 1

        amt_most_common = max(freq.values())
        if len(tasks) % 2 == 0:
            return amt_most_common * n + 1
        else:
            return amt_most_common * n

        