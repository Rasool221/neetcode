# min will be surrounded by bigger and smaller values
# in a rotated arr
# e,g, [3,4,5,6,1,2]
# 1. take midpoint of the arr, for example in above, take 5 (index 2)
# 2. look 2 indexes in both direction, take index of 
# the min number of the 4 numbers as the midpoint,
# set the upper/lower bound depending on what side you take
# - keep a global min

class Solution:
    def findMin(self, nums: List[int]) -> int:
        lower = 0 
        upper = len(nums)-1
        gmin = float('inf')
        
        while lower <= upper:
            m = (lower + upper) // 2

            nm = nums[m]
            nm_l = nums[m-1] # wraps to grab other end
            nm_r = nums[m+1] if m+1 <= len(nums)-1 else nums[0]

            # print(nm_l, nm, nm_r)

            gmin = min(nm_l, nm, nm_r, gmin)

            if nm < nm_l and nm < nm_r:
                break

            if nm < nm_r:
                if m-1 < 0:
                    upper = len(nums) - 1
                    lower = m + 1
                else:
                    upper = m-1
            else:
                if m+1 > len(nums) - 1:
                    lower = 0
                    upper = m-1
                else:
                    lower = m+1

        return gmin



            
