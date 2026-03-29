import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        inner_grids = {}

        # populating maps of sets
        for i in range(10):
            rows[i] = set()
            cols[i] = set()
        
        for i in range(3):
            for j in range(3):
                inner_grids[(i,j)] = set()

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == ".":
                    continue

                if cell in rows[i]:
                    return False

                if cell in cols[j]:
                    return False

                c = math.floor(i/3)
                k = math.floor(j/3)

                if cell in inner_grids[(c,k)]:
                    return False

                rows[i].add(cell)
                cols[j].add(cell)
                inner_grids[(c,k)].add(cell)

        return True
                


