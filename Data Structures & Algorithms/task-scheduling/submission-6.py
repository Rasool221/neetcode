class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        t = 0
        c = 0
        
        # building a frequency map of tasks
        # and counting how many tasks tie for most frequest task
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

            if freq[task] > t:
                t = freq[task]
                c = 1
            elif freq[task] == t:
              c += 1
        
        # if our formula underestimates, the min time to execute
        # all tasks is the amount of tasks!
        return max((t - 1) * (n + 1) + c, len(tasks))
