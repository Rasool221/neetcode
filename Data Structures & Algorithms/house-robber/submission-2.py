# standard dp problem, we can do a bottoms up approach where
# for every item, we would look at i-2 back and add with it robbing 2 houses ago or not robbing 2 houses ago
# if that item doesnt have a house i-2 away, we are forced to keep it as it is 
# then we keep going for every house
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[-1]
        
            