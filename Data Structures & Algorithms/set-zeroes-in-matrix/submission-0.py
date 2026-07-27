"""
we can make 2 passes, 
- first pass: record locations of 0s by setting first index of row & col to 0
- second pass: for every first 0 of row or col, set entire dimension to 0

should be within the contraints of this problem
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for n in range(len(matrix)):
            for m in range(len(matrix[n])):
                # if the col is 0, no need to process cell
                if matrix[0][m] == 0:
                    continue

                k = matrix[n][m]

                if k == 0:
                    matrix[n][0] = 0
                    matrix[0][m] = 0

                    # no need to keep scanning row
                    break

        for n in range(len(matrix)):
            for m in range(len(matrix[n])):
                if matrix[0][m] == 0 or matrix[n][0] == 0:
                    matrix[n][m] = 0