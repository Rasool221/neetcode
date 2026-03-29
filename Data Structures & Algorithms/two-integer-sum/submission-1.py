class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            i_n = nums[i]
            for j in nums:
                if i + j == target:
                    return 