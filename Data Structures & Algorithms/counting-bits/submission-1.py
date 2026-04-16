class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        dp[0] = 0
        offset = 1

        for i in range(n+1):
            if i == 0:
                continue
            
            if i == offset * 2:
                offset = i

            dp[i] = dp[i - offset] + 1

        return dp