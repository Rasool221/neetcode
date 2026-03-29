class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        for c in s:
            if c not in m:
                m[c] = 1
            else:
                m[c] = m[c] + 1

        for c in t:
            if c not in m:
                return False
            elif m[c] == 0:
                return False   
            else:
                m[c] = m[c] - 1

        max_count = max(l for _,l in m.items())
        return max_count == 0