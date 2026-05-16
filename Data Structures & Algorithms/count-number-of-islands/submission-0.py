class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0

        def map_island(i: int, j: int):
            q = [
                (i, j)
            ]
            
            while len(q) > 0:
                pos = q.pop()
                x = pos[1]
                y = pos[0]

                # mutating input so we can save on space
                # of "already visited"
                grid[y][x] = "0"

                # up
                if y > 0 and grid[y - 1][x] == "1":
                    q.append((y - 1, x))
                
                # down
                if y < len(grid) - 1 and grid[y + 1][x] == "1":
                    q.append((y + 1, x))

                # right
                if x < len(grid[y]) - 1 and grid[y][x + 1] == "1":
                    q.append((y, x + 1))

                # left
                if x > 0 and grid[y][x - 1] == "1":
                    q.append((y, x - 1))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                n = grid[i][j]

                # if not a landmass, keep going
                if n == "0":
                    continue

                # mapping this island goes around
                # all surrounding land masses, and marks as 
                # water masses, so we dont loop over them again
                # making our time complexity O(m*n)
                map_island(i, j)

                # for every land mass we encounter in this loop, we know its an island because map_island
                # would get land masses connected to ones we've previously seen
                answer += 1

        return answer