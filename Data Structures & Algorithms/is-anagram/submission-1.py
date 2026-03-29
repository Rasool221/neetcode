class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        for c in s:
            if c not in m:
                m[c] = 1
            else:
                m[c] = m[c] + 1
        
        #print(m)

        for c in t:
            #print(m)
            if c not in m:
                return False
            elif m[c] == 0:
                return False   
            else:
                m[c] = m[c] - 1

        return True