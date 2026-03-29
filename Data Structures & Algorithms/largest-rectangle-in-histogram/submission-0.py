class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        gmax = 0
        for i in range(len(heights)):
            n = heights[i]

            if len(s) == 0:
                s.append(i)
                continue

            gmax = max(n, gmax)

            top = heights[s[-1]] 
            if n >= top:
                s.append(i)
            else:
                while len(s) > 0 and n < top:
                    d = (i - top) + 1
                    gmax = max(n*d, gmax)

                    s.pop()
                    if len(s) > 0:
                        top = heights[s[-1]]

        if len(s) > 0:
            d = len(s)
            h = min(s)
            gmax = max(d*h, gmax)

        return gmax
