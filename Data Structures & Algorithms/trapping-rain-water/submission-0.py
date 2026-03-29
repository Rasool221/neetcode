# iterating solution:
#   left ptr and right ptr
#   right ptr iterates through the array
#   when a bar is found, left pointer is set at bar, right pointer keeps iterating
#   when right pointer reaches a bar that is at least the same height as left bar,
#       add area to counter
#       move left pointer to position

# running through example:
#   iteration 0, left = 0, right = 0, area = 0
#   iteration 1, left = 0, right = 1, area = 0: setting left = 1
#   iteration 2, left = 1, right = 2, area = 0: space += 0  
#   iteration 3, left = 1, right = 3, area = 0: found bar >= left bar, calculating area:
#       area += min(left, right) - space
#       setting left = right = 3
#       space = 0
#   iteration 4, left = 3, right = 4, area = 2, space = 0: setting space += 1
#   iteration 5, left = 3, right = 5, area = 2, space = 1
#   iteration 6, left = 3, right = 6, area = 2, space = 1: setting space += 1
#   iteration 7, left = 3, right = 7, area = 2, space = 2: found bar >= left bar, calculating area:
#   area += min(left, right) - space = 9
#   setting left = right = 7
#   space = 0
#   


# time complexity: 
# O(n), we only iterate through the list once, scales linearly

# space complexity:
# O(1), we store a few variables, nothing that scales linearly with input

class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        area = 0
        space = 0

        for r in range(len(height)):
            rn = height[r]
            ln = height[l]

            # print("-")
            # print("l", l)
            # print("r", r)
            # print("rn", rn)
            # print("ln", ln)

            if ln == 0 and rn > 0:
                l = r
                continue

            if ln > 0 and rn < ln:
                space += rn

            if rn >= ln:
                d = (r - l) - 1
                h = min(ln, rn)
                area += (d * h) - area
                l = r
                space = 0

            # print("area", area)
            # print("space", space)

        return area