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

# what if calc 2 dp arrays, one where we skip robbing 1st and 3rd
# and another where we rob 1st and 3rd but we ignore the last element in the arr
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        # basically the same as house robber one
        def do_dp(n: list[int]) -> int:
            dp = [0] * len(n)
            dp[0] = n[0]
            dp[1] = max(n[0], n[1])
            
            for i in range(2, len(n)):
                dp[i] = max(dp[i - 1], n[i] + dp[i - 2])

            return dp[-1]

        return max(
            do_dp(nums[:-1]),
            do_dp(nums[1:])
        )
