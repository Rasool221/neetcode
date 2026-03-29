class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        gmax = 0
        l = 0
        seen = set()
        for r in range(len(s)):
            c = s[r]
            if c in seen:
                gmax = max(gmax, len(seen))
                seen.clear()
                l += 1
                seen.add(s[l])
            
            seen.add(c)

        return max(gmax, len(seen))