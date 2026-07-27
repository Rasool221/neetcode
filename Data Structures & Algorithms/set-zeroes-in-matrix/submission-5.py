"""
we can make 2 passes, 
- first pass: record locations of 0s by setting first index of row & col to 0
- second pass: for every first 0 of row or col, set entire dimension to 0

should be within the contraints of this problem
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # whether the top left flag
        # is inheritly flagged 0
        og_topleft_flag = False

        for n in range(len(matrix)):
            for m in range(len(matrix[n])):
                k = matrix[n][m]

                if k == 0:
                    matrix[n][0] = 0
                    matrix[0][m] = 0

                    # top left cell can be flagged as 0
                    # organically if any cells on first row are 0s
                    if m == 0:
                        og_topleft_flag = True

        # iterate row-wise backwards because
        # the first column can be ambigious
        for n in range(len(matrix) -1, -1, -1):
            for m in range(len(matrix[n]) - 1, -1, -1):
                if matrix[n][0] == 0:
                    matrix[n][m] = 0

                if matrix[0][m] == 0 and not (m == 0 and not og_topleft_flag):
                    matrix[n][m] = 0
