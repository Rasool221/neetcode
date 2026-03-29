class Solution:
    def isHappy(self, n: int) -> bool:
        k = n % 10
        n = n // 10
        ans = k ** 2

        while k != 0:
            k = n % 10
            n = n // 10
            ans += k ** 2

        return ans == k