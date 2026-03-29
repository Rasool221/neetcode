# find min in list O(lgn)
# by finding min you can find offset of rotation
# then apply that to translate between actual indices and normal
# indices

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1

        while lower != upper:
            m = (lower + upper) // 2
            nm = nums[m]
            n_upper = nums[upper]

            # if mid point is larger than upper 
            # bound, the min is to the right
            # else its to the left
            if nm > n_upper:
                lower = m + 1
            else:
                upper = m

        rotation_offset = lower
        if target == nums[rotation_offset]:
            return rotation_offset

        def get_real_index(adjusted_index: int) -> int:
            real_index = adjusted_index + rotation_offset
            if real_index > len(nums) - 1:
                real_index = real_index - (len(nums) - 1)
            return real_index

        # real:     [3,4,5,6,1,2]
        # adjusted: [1,2,3,4,5,6]
        lower = 0
        upper = len(nums) - 1

        while lower <= upper:
            m = (lower + upper) // 2
            nm = nums[get_real_index(m)]

            if nm == target:
                return m
            
            if nm > target:
                lower = m + 1
            else:
                upper = m - 1

        return -1
            