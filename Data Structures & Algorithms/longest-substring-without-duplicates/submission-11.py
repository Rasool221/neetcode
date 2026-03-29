class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        gmax = 0
        l = 0
        seen = set()
        for r in range(len(s)):
            c = s[r]
            if c in seen:
                while c in seen:
                    seen.remove(s[l])
                    l += 1
            
            seen.add(c)
            gmax = max(gmax, r - l + 1)

        return max(gmax, len(seen))