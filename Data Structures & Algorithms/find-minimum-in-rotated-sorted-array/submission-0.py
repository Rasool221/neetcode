# min will be surrounded by bigger and smaller values
# in a rotated arr
# e,g, [3,4,5,6,1,2]
# 1. take midpoint of the arr, for example in above, take 5 (index 2)
# 2. look 2 indexes in both direction, take index of 
# the min number of the 4 numbers as the midpoint,
# set the upper/lower bound depending on what side you take
# - keep a global min

# ahh i think i get it. we have to keep searching for the largest number,

class Solution:
    def findMin(self, nums: List[int]) -> int:
        lower = 0 
        upper = len(nums)-1
        largest_index = 0
        
        while lower <= upper:
            m = (lower + upper) // 2

            nm = nums[m]
            nm_l = nums[m-1] # wraps to grab other end
            nm_r = nums[min(m+1, len(nums)-1)]

            # print(nm_l, nm, nm_r)

            # objective: chase the largest number

            # if cur number is bigger than both
            # numbers around it, we found the max
            if nm > nm_r and nm > nm_l:
                largest_index = m
                break

            if nm_l < nm:
                lower = m+1
            else:
                upper = m-1

        if largest_index == len(nums) - 1:
            return nums[0]
        
        if largest_index == 0:
            return nums[len(nums)-1]
        
        return nums[largest_index+1]



            
