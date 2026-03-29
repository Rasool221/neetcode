class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # stores (height, index)
        gmax = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                height, index = stack.pop()
                gmax = max(gmax, height * (i - index))
                start = index
            stack.append((h, start))

        for h, index in stack:
            gmax = max(gmax, h * (len(heights) - index))

        return gmax