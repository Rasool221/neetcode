class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)

        dp[0] = cost[0] 
        dp[1] = cost[1]

        for i in range(len(dp)):
            if i == 0 or i == 1:
                continue
            
            c = cost[i]
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

            if i == len(dp) - 1 and dp[i-1] < dp[i]:
                dp[i] = dp[i-1]

        print(dp)

        return dp[len(dp)-1]

