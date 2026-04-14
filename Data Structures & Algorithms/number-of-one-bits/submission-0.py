class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            m = 1 << i
            if m & n:
                count += 1
        return count