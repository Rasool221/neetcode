class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = i + 1
            k = nums[i]

            if n ^ k != 0:
                return k    

        return -1