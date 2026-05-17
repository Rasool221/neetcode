"""
    let's represent the input with inf 

    Example 1
    Input: [
        [inf, -1,  0,   inf],
        [inf, inf, inf,  -1],
        [inf, -1,  inf,  -1],
        [0,   -1,  inf, inf]
    ]

    Output: [
        [3,-1,0,1],
        [2,2,1,-1],
        [1,-1,2,-1],
        [0,-1,3,4]
    ]

    i think we can simply run dfs on the grid, however,
    i dont think that would yield O(m*n) time complexity,
    more like O(m*n^4) since worst case is we can move in any direction
    looking for a chest?
`
    but that's if search at every cell, and we're not, only on cells marked with 'inf'

    i think that's too complicated. we should start from where the chests are and just use BFS
    i think we need to first map out where chests are in an initial run, then use BFS in one more pass to explore
    from chests out and modify grid in place to how far away from chests. let's use a deque and append() & popleft() for a FIFO queue
    of cells to explore and mark distance
"""

from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        chests = []
        inf = 2147483647

        # first pass, figure out where the chests are
        for m in range(len(grid)):
            for n in range(len(grid[m])):
                c = grid[m][n]
                if c == 0:
                    chests.append((m, n))

        q = deque([])

        # populating our deque with chest locations
        for chest in chests:
            q.append(chest)

        def can_visit(m: int, n: int) -> bool:
            c = grid[m][n]
            return c != -1 and c == inf

        # second pass, BFS outwardly from chests
        while len(q) > 0:
            t = q.popleft()
            
            m = t[0]
            n = t[1]

            # this # represents how far away from nearest chest
            # if its a chest itself (first iter) it says 0
            cur = grid[m][n]

            # for every adjacent pos, we do 2 things:
            # 1. explore as long as adjacent positions are in bound and not -1
            # 2. modify adjacent pos in grid of distance from chest

            # left
            if n > 0 and can_visit(m, n - 1): 
                grid[m][n - 1] = cur + 1
                q.append((m, n - 1))

            # right
            if n < len(grid[m]) - 1 and can_visit(m, n + 1):
                grid[m][n + 1] = cur + 1
                q.append((m, n + 1))

            # up
            if m > 0 and can_visit(m - 1, n):
                grid[m - 1][n] = cur + 1
                q.append((m - 1, n))

            # down
            if m < len(grid) - 1 and can_visit(m + 1, n):
                grid[m + 1][n] = cur + 1
                q.append((m + 1, n))
