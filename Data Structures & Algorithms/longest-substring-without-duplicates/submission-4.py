# "zxyzxyz"
# l = r = z, seen = {}
# l = z, r = x, seen = {"z"}

# "dvdf"
# l = r = d, seen = {"d"}
# l = d, r = v, seen = {"d", "v"}
# l = d, r = d, seen = {}, gmax = 2
# l = v, r = d, seen = {"d"}

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
                seen = set()
                seen.add(s[l])

            if r <= len(s) - 1:
                seen.add(s[r])

            r += 1

        return max(gmax, len(seen))