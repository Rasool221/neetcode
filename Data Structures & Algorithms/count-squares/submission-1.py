"""
the recommended complexities are: 
* O(1) time on add()
* O(n) time & space on count()

since count() is called with a point [x, y] i think this makes
the problem easier

so im thinking every time count(point) is called, we search outwards from
the given point going in all 4 diagonal directions. once we find a point at a 
diagonal direction, we then assert that points exist in axis reaching back. as 
soon as we cannot find a point in the paths back, we stop, as that no longer can be a
square

if no point is found, we keep going, in case there is a square larger than a size of 1
however we need some heuristic to know if there are any points in any diagonal direction
so we know when to stop. hmm

i think we can just have a gobal set

ahhh i maybe overcomplicating this, because i am assuming that there will be points between each
corner which is likely not the case. therefore, i can just look at diagonals and attempt to find other diagonals
that forms a square. also, i will keep track of duplicate points because if they land on a square
they contribute to the total amount of squares

the one thing i cannot stop thinking about that isnt addressed in this
solution is what if a square already exists before count() is called?
oh well, i will just see what happens in that case when i get to it
"""
class CountSquares:
    def __init__(self):
        self.m = {} # (x, y): amount that point is added

    # using simple property of a square we
    # know if a square is a diagonal
    def are_diagonals(self, x1: int, x2: int, y1: int, y2: int) -> int:
        x_diff = abs(x1 - x2)
        y_diff = abs(y1 - y2)
        return x_diff if x_diff == y_diff else -1

    def add(self, point: List[int]) -> None:
        x, y = point
        e = (x, y)

        self.m[e] = self.m.get(e, 0) + 1

    def count(self, point: List[int]) -> int:
        x, y = point

        answer = 0

        for point2, freq in self.m.items():
            x2, y2 = point2

            d = self.are_diagonals(x, x2, y, y2)

            # points that are not diagonals
            # will return a distance of -1
            # otherwise, we use distance to help
            # us figure out the other 2 corners of a square
            if d == -1:
                continue

            # top-right to bottom-left 
            # or bottom-left to top-right
            if (x > x2 and y > y2) or (x < x2 and y < y2):
                # anchoring on top-right
                anchor_x = x if x > x2 else x2
                anchor_y = y if y > y2 else y2


                top_left = (anchor_x - d, anchor_y)
                bottom_right = (anchor_x, anchor_y - d)

                if top_left in self.m and bottom_right in self.m:
                    answer += (
                        self.m[top_left] *
                        self.m[bottom_right] *
                        self.m[(x2, y2)]
                    )

            # bottom-right to top-left
            # or top-left to bottom-right
            elif (x > x2 and y < y2) or (x < x2 and y > y2):
                # anchoring on top-left
                # as our reference point
                anchor_x = x if x < x2 else x2
                anchor_y = y if y > y2 else y2

                top_right = (anchor_x + d, anchor_y)
                bottom_left = (anchor_x, anchor_y - d)

                if top_right in self.m and bottom_left in self.m:
                    answer += (
                        self.m[top_right] *
                        self.m[bottom_left] *
                        self.m[(x2, y2)]
                    )

        return answer



            
