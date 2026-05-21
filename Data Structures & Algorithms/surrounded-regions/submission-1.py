# i think we would totally skip looking at any cell
# on the edges, (first and last element of m and n)
# what we do is log position of each O in a first pass
# then push to a queue
# i think in the queue we should store O positions as coords of
# [top_left, bottom_right]. they will always equal eachother after the first 
# pass, indicating its 1 square large

# then in a second pass we look at the queue, and perform BFS

# i think when we process Os in a queue, we should
# check if Os have the following cases:
# 1. if the O has a top, left, and top left O element, we extend 
#    the top left coord to the top left O of current one and push to queue
#    then skip rest of processing this one 
# 2. if the O has a right, bottom, and bottom right O element, we extend
#    the bottom right coord to the bottom right O element of current one and push to queue,
#    then skip rest of processing this one 
# 3. otherwise, using top_left and bottom_right coords we can check if all elements
#    that surround top left and bottom right (top and left of bottom right) & (bottom and right of top left),
#    if so, we turn all Os between top left and bottom right

# OKAY CLEARLY I WAS WAYYYYY OFF
# i thought that Os can form squares, i completely misunderstood the problem
# its any connection region of Os
# i think in this case, we will do a first pass on the borders ONLY
# if the cell is an O, we will mark it something temp, like "#"
# in a second pass, we do a BFS on every marked O position and try to move inward,
# as we encounter Os, we can modify them inplace as Xs (because those cells ARENT surrounded)
# and we flop back the "#" cells back to "O"

from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        q = deque([])

        ROWS = len(board)
        COLS = len(board[0])

        # first pass, record positions of Os in border of board, 
        # mark them as temp and push into queue
        for n in range(COLS):
            top = board[0][n]
            bottom = board[ROWS - 1][n]

            if top == "O":
                q.appendleft((0, n))
                board[0][n] = "#"  # mark safe

            if bottom == "O":
                q.appendleft((ROWS - 1, n))
                board[ROWS - 1][n] = "#"  # mark safe

        for m in range(ROWS):
            left = board[m][0]
            right = board[m][COLS - 1]

            if left == "O":
                q.appendleft((m, 0))
                board[m][0] = "#"

            if right == "O":
                q.appendleft((m, COLS - 1))
                board[m][COLS - 1] = "#"

        # second pass, BFS from all border-connected Os
        # we propagate "safe" marking inward
        while len(q) > 0:
            r, c = q.popleft()

            # check 4 directions (NOT diagonals)
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # if inside bounds and still O, mark safe and continue BFS
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    if board[nr][nc] == "O":
                        board[nr][nc] = "#"
                        q.appendleft((nr, nc))

        # final pass:
        # all remaining O -> surrounded -> turn into X
        # all S -> restore back to O
        for m in range(ROWS):
            for n in range(COLS):
                if board[m][n] == "O":
                    board[m][n] = "X"
                elif board[m][n] == "#":
                    board[m][n] = "O"