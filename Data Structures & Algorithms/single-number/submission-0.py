class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_total = 0

        for i in range(len(nums)):
            n = nums[i]
            xor_total ^= n

        return xor_total