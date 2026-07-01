# i think we can trivially do this by scanning
# through the list 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i != nums[i]:
                return i

        return -1