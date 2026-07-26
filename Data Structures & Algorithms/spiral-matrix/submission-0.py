class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix[0])
        n = len(matrix)

        answers = []

        margins = [
            0, # right
            0, # bottom
            0, # left
            0, # top
        ]

        size = [
            m,
            n,
        ]

        directions = [
            [ 0,  1], # right
            [ 1,  0], # down
            [ 0, -1], # left
            [-1,  0], # up
        ]

        i = 0
        j = -1
        direction = 0
        while len(answers) < m * n:
            run = size[direction % 2] - (margins[direction] + margins[(direction + 2) % 4])
            for _ in range(run):
                # print(f"{i=} {j=} {run=}")
                di, dj = directions[direction]
                i += di
                j +=dj
                answers.append(matrix[i][j])
            margins[(direction - 1) % 4] += 1
            direction = (direction + 1) % 4
        
        return answers