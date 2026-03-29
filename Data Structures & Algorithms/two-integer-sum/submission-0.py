class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            n = nums[i]
            if n in num_map:
                return [num_map[n], i]
            else:
                diff = abs(target - n)
                num_map[diff] = i