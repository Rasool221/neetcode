class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        counted = set()

        def dfs(grid, i, j) -> int:
            if i < 0 or i > len(grid) - 1:
                return 0
            if j < 0 or j > len(grid[i]) - 1:
                return 0
            
            cell = grid[i][j]

            if cell == 0:
                return 0
            
            if (i, j) in counted:
                return 0
            
            counted.add((i, j))

            amt_right = dfs(grid, i + 1, j)
            amt_left = dfs(grid, i - 1, j)
            amt_down = dfs(grid, i, j + 1)
            amt_up = dfs(grid, i, j - 1)

            return (amt_right + amt_left + amt_down + amt_up) + 1

        largest = 0

        for i in range(len(grid)):
            row = grid[i]
            for j in range(len(grid[i])):
                cell = grid[i][j]
                
                if cell == 0:
                    continue

                if (i, j) in counted:
                    continue

                total = dfs(grid, i, j)
                if total > largest:
                    largest = total

        return largest
            


                
                

                