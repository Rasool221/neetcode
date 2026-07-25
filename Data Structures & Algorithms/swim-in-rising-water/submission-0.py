# the premise sounds straightforward
# i keep a counter for time which increments every "step"
# now i need to decide what kind of path finding alg ill use to traverse this matrix, im thinking
# maybe DFS that tracks the step state, either wait or continue. however, i think that's worse than 
# the suggested time complexity which os O((2^n)logn), the backtracking solution would be O(2^n) i believe

# now, what about BFS, where we can explore paths depending on an incrementing T (for time?).
# i think that sounds natural at the moment for this. our goal is to get to bottom right using only
# vertical or horizontal movements. i think a solution is also guarunteed, its just a matter of time

# working out the first example:
# t = 0 
# 0     1
# 2     3

# t = 1
# 0 ->  1
# 2     3

# t = 2
# 0 ->  1
# |
# v
# 2     3

# t = 3
# 0 -> 1
# |    | 
# v    v
# 2 -> 3
# answer is 3 because t = 3 when we reached bottom right

# the one thing im thinking about is when im scanning for potential next place to go
# i need to ensure everything around me (grid positions) are also being updated, as they are 
# essentially becoming "shallower" (filling up with 1 units of water per tick/step)

# that said, it would be inefficient to make a copy of the matrix and iterate it every step
# to increase base water level by 1. instead i think i can just dynamically subtract t from every cell
# and we can move to it if c - t <= 0

# now i think that makes sense and we can check if bottom right 
# cell has a value of <= 0, in which case we can stop, however
# we also need to check if a path of water has made it to the bottom right cell

# i also think we need to track more than 1 paths of water down to the bottom right cell
# hmmm

# ah, what if we keep it simple, and do BFS, and at every step, decrement the grid cells by 1? 
# i think that matches our time and space constraints, and in fact i think we can save on space to O(1)
# by modifying the grid
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        t = 0
        
        def reached_end(i: int, j: int) -> bool:
            return (
                i == len(grid) - 1 and
                j == len(grid[i]) - 1
            )

        h = [(0, 0, 0)] # start at top left, with water level 0

        MOVEMENTS = [
            (-1, 0), # up
            (1, 0), # down
            (0, -1), # left
            (0, 1), # right
        ]
    
        visited = set()

        while h:
            level, i, j = heapq.heappop(h)
            t = max(level, t)
            visited.add((i, j))

            # base case, if we've reached the end, we can return t
            if reached_end(i, j):
                return t

            # see if we can move in any direction
            # and if so, add to our heap and pop top, (then add to visited)
            for i_d, j_d in MOVEMENTS:
                i_n = i + i_d
                j_n = j + j_d

                # if we can move are 3 checks:
                # - out of bounds check
                # - is spot already visited
                if (
                    (i_n <= len(grid) - 1 and i_n >= 0) and
                    (j_n <= len(grid[i_n]) - 1 and j_n >= 0) and
                    (i_n, j_n) not in visited
                ):  
                    l = grid[i_n][j_n]
                    heapq.heappush(h, (l, i_n, j_n))


        return t
            