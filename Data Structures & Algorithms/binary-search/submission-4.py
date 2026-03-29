class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1

        while lower <= upper:
            midpoint = (upper - lower) // 2
            midpoint += lower

            if nums[midpoint] == target:
                return midpoint

            if nums[midpoint] > target:
                upper = midpoint - 1

            if nums[midpoint] < target:
                lower = midpoint + 1


        return -1
