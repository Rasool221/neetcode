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
class Pos:
    def __init__(self, top_left: tuple[int, int], bottom_right: tuple[int, int]):
        self.top_left = top_left
        self.bottom_right = bottom_right
        
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque([])

        # first pass, record positions of Os, skipping edges
        # of the board
        for m in range(1, len(board) - 1):
            for n in range(1, len(board[m]) - 1):
                c = board[m][n]
                if c == "O":
                    q.appendleft(
                        Pos(
                            (m, n),
                            (m, n)
                        )
                    )

        # second pass, propogate outwards and either 
        # combine Os into squares, or process edges and change
        # the Os into Xs
        while len(q) > 0:
            # its safe to access top left and bottom right
            # diagonals of this element because we skipped edges
            # when we've populated this queue
            top = q.popleft()
            top_left = top.top_left
            bottom_right = top.bottom_right

            # check if O extends top left, if so, extend it
            if (
                board[top_left[0] - 1][top_left[1] - 1] == "O" and # diagonal top left
                board[top_left[0] - 1][top_left[1]] == "O" and # top
                board[top_left[0]][top_left[1] - 1] == "O" # left
            ):  
                q.appendleft(
                    Pos(
                        (top_left[0] - 1, top_left[1] - 1), # new top left
                        bottom_right # same bottom right
                    )
                )
            # check if O extends bottom right, if so, extend it
            elif (
                board[bottom_right[0] + 1][bottom_right[1] + 1] == "O" and # diagonal bottom right
                board[bottom_right[0] + 1][bottom_right[1]] == "O" and # bottom
                board[bottom_right[0]][bottom_right[1] + 1] == "O" # right
            ):
                q.appendleft(
                    Pos(
                        top_left, # same top left
                        (bottom_right[0] + 1, bottom_right[0] + 1) # new bottom right
                    )
                )
            # otherwise if we're at bottom right and top left edges, for either single 
            # Os or combined Os, we check if their edges are Xs (without diagonals), and if so
            # we will modify them in place as Os
            else:
                # we will now check top & bottom if they're surrounded by Xs
                # at the same time
                is_surrounded = True
                for n in range(top_left[1], bottom_right[1]): # x1 -> x2
                    top_cell = board[top_left[0] - 1][n]
                    bottom_cell = board[bottom_right[0] + 1][n]

                    if top_cell != "X" or bottom_cell != "X":
                        is_surrounded = False
                        break

                for m in range(top_left[0], bottom_right[0]): # y1 -> y2
                    left_cell = board[m][top_left[1] - 1]
                    right_cell = board[m][bottom_right[1] + 1]

                    if left_cell != "X" or right_cell != "X":
                        is_surrounded = False
                        break

                # now if this pos is surrounded, we can update all cells within the pos
                # to Os
                if is_surrounded:
                    for m in range(top_left[0], bottom_right[0]):
                        for n in range(top_left[1], bottom_right[1]):
                            board[m][n] = "X"
