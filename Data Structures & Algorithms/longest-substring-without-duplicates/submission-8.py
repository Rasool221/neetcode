class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        gmax = 0
        l = r = 0 
        seen = set()
        while r <= len(s) - 1 and l <= len(s) - 1:
            if s[r] in seen:
                l += 1
                r = l + 1
                gmax = max(gmax, len(seen))
                seen.clear()
                seen.add(s[l])

            
            seen.add(s[r])

            r += 1

        return max(gmax, len(seen))