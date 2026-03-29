class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1

        while True:
            if upper - lower == 0:
                if nums[lower] == target:
                    return lower

                break

            if upper - lower == 1:
                if nums[upper] == target:
                    return upper

                if nums[lower] == target:
                    return lower

                break

            midpoint = (upper - lower) // 2
            midpoint += lower

            if nums[midpoint] == target:
                return midpoint

            if nums[midpoint] > target:
                upper = midpoint 

            if nums[midpoint] < target:
                lower = midpoint

        return -1
