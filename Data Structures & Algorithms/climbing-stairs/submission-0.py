class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1 # one way to get to 1
        dp[1] = 2 # two ways to get to 2

        # print(dp)
        # and so forth...
        for i in range(len(dp[2:])):
            c = i+2
            dp[c] = dp[c-1] + 1
            dp[c] = dp[c-2] + 2
            # print(c)
        # print(dp)
        return dp[n-1]