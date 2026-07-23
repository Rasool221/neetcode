# well this is based on properties of matrices, 
# where any rotation is a composition of two reflections

# for clockwise 90 degree rotation, we reflect diagonally, then vertically

# so that becomes:
# - transpose
# - reflect vertically in the middle

# for our transpose:
# in order to not undo swaps, we only iterate over 
# a top triangle of the matrix and perform swaps

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # step 1, transpose
        # transposing a matrix is simply reversing 
        # indices, so (i, j) become (j, i)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # step 2, reflecting matrix vertically
        # this is basically just reversing each row
        for i in range(n):
            matrix[i] = matrix[i][::-1]
        