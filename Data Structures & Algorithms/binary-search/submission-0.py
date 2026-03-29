class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1

        while True:
            midpoint = (upper - lower) // 2

            if nums[midpoint] > target:
                lower = midpoint 

            if nums[midpoint] < target:
                upper = midpoint
            
            if nums[midpoint] == target:
                return midpoint
            
            print(nums)

            if upper - lower == 0 and nums[midpoint] != target:
                return -1
        
        return -1
