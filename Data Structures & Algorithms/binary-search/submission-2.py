class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1

        while True:
            midpoint = (upper - lower) // 2
            midpoint += lower

            if nums[midpoint] == target:
                return midpoint

            if upper == midpoint or lower == midpoint:
                break

            if nums[midpoint] > target:
                upper = midpoint 

            if nums[midpoint] < target:
                lower = midpoint
            
            

        return -1
