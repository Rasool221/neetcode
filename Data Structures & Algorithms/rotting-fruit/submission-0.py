# alright so im thinking for this one ill do the following:
# - do a first pass, count how many good bananas there are & note the locations of rotten bananas 
# - insert their positions into a FIFO queue 
# - keep count of minutes starting from 0
# - enter iteration until the queue is empty. for each iteration, pop off the queue,
#   make adjacent bananas rotten, then add adjacent bananas to the queue
# - we continue until queue is empty
# - after the iteration if we've made all bananas rotten, we can return the count. if we've missed some
#   we will return -1 (some bananas arent adjacent to others)
# i think we can simply use BFS and a FIFO queue to solve this outwardly from the rotten bananas

# so its working but can take extra minutes because two or more bananas can go rotten and we're counting minutes 
# for every banana made rotten, not for all adjacent bananas made rotten
# so for every iteration in the while loop we pull all off the queue and process all, then push back onto the queue
# or we make our minute counting a little bit smarter.
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        # first pass, count good bananas
        amt_good_bananas = 0
        for m in range(len(grid)):
            for n in range(len(grid[m])):
                c = grid[m][n]
                if c == 1:
                    amt_good_bananas += 1
                elif c == 2:
                    q.appendleft((m,n))


        bananas_made_rotten = 0
        minutes = 0

        # while the queue can be populated,
        # pop off the entire queue and process at once, then add to the queue
        # after all adjacent bananas have been processed
        while len(q) > 0:
            adjacent_bananas = list(q)
            q.clear()

            # some bananas can add the same adjacent banana,
            # so we need a set to ensure we're adding unique bananas
            # to the queue only
            bananas_to_add = set()

            for banana in adjacent_bananas:
                m = banana[0]
                n = banana[1]

                # up
                if m > 0 and grid[m - 1][n] == 1:
                    grid[m - 1][n] = 2
                    bananas_to_add.add((m - 1, n))
                    bananas_made_rotten += 1
    
                # down 
                if m < len(grid) - 1 and grid[m + 1][n] == 1:
                    grid[m + 1][n] = 2
                    bananas_to_add.add((m + 1, n))
                    bananas_made_rotten += 1
    
                # left 
                if n > 0 and grid[m][n - 1] == 1:
                    grid[m][n - 1] = 2
                    bananas_to_add.add((m, n - 1))
                    bananas_made_rotten += 1
    
                # right
                if n < len(grid[m]) - 1 and grid[m][n + 1] == 1:
                    grid[m][n + 1] = 2
                    bananas_to_add.add((m, n + 1))
                    bananas_made_rotten += 1

            bananas_to_add = list(bananas_to_add)
            for banana_pos in bananas_to_add:
                q.appendleft(banana_pos)               
    
            if len(q) > 0:
                minutes += 1


        if bananas_made_rotten == amt_good_bananas:
            return minutes

        return -1