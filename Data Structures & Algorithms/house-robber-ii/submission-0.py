# this is a continuation on house robber one which i solved 
# with bottoms up dp, counting best value which is the max of 
# keeping the money you have so far or money collected from robbing house i - 2.

# the only difference with this problem is that the first house and last house
# in the input array are adjacent, so we cant rob the first house AND last house

# the path of robbing first house and last house are the even number indices, so we skip those?
# or at the very least we start rob max(3rd house, 1st + 3rd house?)

# what would the recurrance relation be?
# dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
# above is original recurrance relation, max of robbing this house or not robbing and moving on 
# i think we just eliminate robbing house 0 and start with house 1 and forward.

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1] # do not rob house 0, so no max here.
        dp[2] = max(nums[1], nums[2]) # start from robbing house 2 or house 3, but not house 1 to eliminate the circular constraint

        for i in range(4, len(nums)):
            # same recurrance relation as house robber 1, either do not rob current house or sub last non adjacent house (i - 2)
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]
