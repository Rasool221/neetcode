# i think this problem is very similar to cell phone digits problem where 
# we have to for loop recursive backtracking down the the decision tree
# we also would pass down the current state of the board, which squares we cannot place the 
# queen on. 
# we would build row by row. 
# we can only place 1 queen per row
# at each square of a row, we would check if a previously placed queen would attack the current queen
# if so, we move to the next square. if not, we place it, and keep going down the tree. the recrusiveness would
# come back to that point in the tree if that route didnt work out downstream

# checking horizontal and vertical is trivial, lets figure out horizontal
#   0 1 2 3
# 0 . Q . . (1, 0) -> diagonals are (0, 1), (2, 1), (3, 2)
# 1 . . . Q
# 2 Q . . .
# 3 . . Q .


# actually we dont need to keep horizontal checks, because we're only placing 1 queen per row. 
# but we need to keep vertical and diagonal of course
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answers = []

        # i is the row [0, n-1]
        # q are coordinates of queens already placed
        # v are vertical indexes other queens are on
        # d are diagonal indexes other queens are on AND covering
        def recurse(i: int, v: set, d: set[tuple], board: list[str]):
            nonlocal answers

            # print(f"{i=} {board=}")

            # base case: we've reached the end
            if i >= n:
                answers.append(board)
                return

            # use temp params to pass down the tree in case we 
            # come back up to current node and move to next position,
            # as to not pollute the state
            t_v = v.copy()
            t_d = d.copy()

            # try to place the queen on the current row
            row = ""
            for j in range(n):
                pos = (j, i)

                # check verticals & horizontals
                if j in t_v:
                    row += "."
                    continue
                
                # check diagonals
                if (j, i) in t_d:
                    row += "."
                    continue

                # add queen to position
                row += "Q"

                # add any more dots we were missing
                if j < n - 1:
                    row += "." * (n - 1 - j)

                # add vertical position so we dont place 
                # queens in this rank anymore
                t_v.add(j)

                # up, right [x + 1, y - 1]
                x, y = j, i
                while x <= n - 1 and y >= 0:
                    x += 1
                    y -= 1
                    t_d.add((x, y))

                # down, right [x + 1, y + 1]
                x, y = j, i
                while x <= n - 1 and y <= n - 1:
                    x += 1
                    y += 1
                    t_d.add((x, y))

                # left, down [x - 1, y + 1]
                x, y = j, i
                while x >= 0 and y <= n - 1:
                    x -= 1
                    y += 1
                    t_d.add((x, y))

                # up, left [x - 1, y - 1]
                x, y = j, i
                while x >= 0 and y >= 0:
                    x -= 1
                    y -= 1
                    t_d.add((x, y))

                # start decision tree at this point for next row
                # use temp vars unique to this node so if this path doesnt work
                # we dont pollute state
                recurse(i + 1, t_v, t_d, board + [row])

                # reset temp vars and row
                t_v = v.copy()
                t_d = d.copy()
                row = "." * (j + 1)


        recurse(0, set(), set(), [])
        return answers
                

                
                
            