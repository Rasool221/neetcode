# standard dp problem, we can do a bottoms up approach where
# for every item, we would look at i-2 back and add with it robbing 2 houses ago or not robbing 2 houses ago
# if that item doesnt have a house i-2 away, we are forced to keep it as it is 
# then we keep going for every house
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(len(nums)):
            prev = 0
            if i > 1:
                prev = nums[i - 2]

            nums[i] = max(nums[i], prev + nums[i])

        return max(nums[-1], nums[-2])
        
            