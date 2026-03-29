class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            ln = heights[l]
            rn = heights[r]

            area = min(ln, rn) * (r - l)
            
            if area > max_area:
                max_area = area            

            if ln > rn:
                r -= 1
            elif rn > ln:
                l += 1
            else:
                l += 1
                r -= 1

        
        return max_area