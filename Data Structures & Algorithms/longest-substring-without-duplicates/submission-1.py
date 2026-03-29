class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        gmax = 0
        for i in range(len(s)):
            c = s[i]
            if c in seen:
                gmax = max(gmax, len(seen))
                seen = set()

            seen.add(c)
            
        return max(gmax, len(seen))
