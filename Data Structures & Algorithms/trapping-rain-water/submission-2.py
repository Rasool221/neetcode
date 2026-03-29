class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        suffix = [0] * len(height)
        suffix[-1] = height[-1]

        for i in range(len(height)):
            n = height[i]
            if i == 0:
                prefix.append(n)
                continue
            
            last_n = prefix[i-1]
            prefix.append(max(n, last_n))

        for i in range(len(height) - 2, -1, -1):
            suffix[i] = max(height[i], suffix[i+1])

        area = 0
        for i in range(len(height)):
            n = height[i]

            left = prefix[i]
            right = suffix[i]

            if n == left or n == right:
                continue

            area += min(left, right) - n

        return area

        