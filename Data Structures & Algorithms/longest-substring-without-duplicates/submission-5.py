class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        gmax = 0
        l = 0 
        seen = set()
        for r in range(len(s)):
            if s[r] in seen:
                l += 1
                r = l + 1
                gmax = max(gmax, len(seen))
                seen = set()
                seen.add(s[l])

            if r <= len(s) - 1:
                seen.add(s[r])

            r += 1

        return max(gmax, len(seen))