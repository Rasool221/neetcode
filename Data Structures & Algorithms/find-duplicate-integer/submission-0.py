class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == 0:
                continue

            n = nums[i]
            pn = nums[i-1]
            if n == pn:
                return n

        return -1
            