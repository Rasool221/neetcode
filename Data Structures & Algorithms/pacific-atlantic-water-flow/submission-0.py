# alright so for this one ill do the following:
# - need to find cells where water can flow to BOTH pacific and atlantic
# - water flows from high to low (or equal), so a cell drains to an ocean if theres a 
#   path of non-increasing heights from it to that ocean's edge
# - brute force would be: for every cell, BFS downhill and see if it hits each ocean. wasteful.
# - smarter: reverse the flow. start AT each ocean and walk UPHILL (or flat) inward.
#   every cell we can reach this way is a cell that couldve drained TO that ocean
# - do this twice: once seeded from pacific edges (top row + left col),
#   once from atlantic edges (bottom row + right col)
# - the answer is the intersection: cells reachable from both
# - pacific touches top + left edges, atlantic touches bottom + right edges (not just corners!)
# - neighbor rule when walking inward: we can step to a neighbor if neighbor_height >= current_height
#   (because in real flow, water wouldve come down from there to us)
# - use a visited set per ocean, seed it with all edge cells upfront so we dont have to special-case them
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        
        # bfs starting from a list of edge cells touching one ocean
        # returns the set of all cells that can drain to that ocean
        def bfs(starts):
            q = deque()
            reachable = set()
            # seed the queue and visited set with all starting edge cells
            for pos in starts:
                reachable.add(pos)
                q.appendleft(pos)
            
            while len(q) > 0:
                cell = q.pop()
                m = cell[0]
                n = cell[1]
                current_height = heights[m][n]
                
                # up
                # we can walk to this neighbor if its height is >= ours
                # (meaning in real flow, water from there couldve come down to us)
                if m > 0 and (m - 1, n) not in reachable and heights[m - 1][n] >= current_height:
                    reachable.add((m - 1, n))
                    q.appendleft((m - 1, n))
                
                # down
                if m < rows - 1 and (m + 1, n) not in reachable and heights[m + 1][n] >= current_height:
                    reachable.add((m + 1, n))
                    q.appendleft((m + 1, n))
                
                # left
                if n > 0 and (m, n - 1) not in reachable and heights[m][n - 1] >= current_height:
                    reachable.add((m, n - 1))
                    q.appendleft((m, n - 1))
                
                # right
                if n < cols - 1 and (m, n + 1) not in reachable and heights[m][n + 1] >= current_height:
                    reachable.add((m, n + 1))
                    q.appendleft((m, n + 1))
            
            return reachable
        
        # pacific touches the top row and left column
        pacific_starts = []
        for n in range(cols):
            pacific_starts.append((0, n))
        for m in range(rows):
            pacific_starts.append((m, 0))
        
        # atlantic touches the bottom row and right column
        atlantic_starts = []
        for n in range(cols):
            atlantic_starts.append((rows - 1, n))
        for m in range(rows):
            atlantic_starts.append((m, cols - 1))
        
        pacific_reachable = bfs(pacific_starts)
        atlantic_reachable = bfs(atlantic_starts)
        
        # the answer is cells that can drain to both oceans
        result = []
        for cell in pacific_reachable & atlantic_reachable:
            result.append([cell[0], cell[1]])
        return result