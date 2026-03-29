# n = 2
# [1, 2] <- 2 ways to get to 2, adding 1, and adding 2

# n = 4
# init [1, 2] <- start with 2 
# [0,2,2] <-- 3 is an odd number, the only way to reach it 
# 
# [0,2,2,5]

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [0] * n
        dp[0] = 1 # one way to get to 1
        dp[1] = 2 # two ways to get to 2

        # and so forth...
        for i in range(len(dp[2:])):
            c = i+2
            dp[c] += dp[c-1]
            dp[c] += dp[c-2]

        
        return dp[n-1]