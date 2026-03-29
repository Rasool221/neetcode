class Solution:
    def minWindow(self, s: str, t: str) -> str:    
        l = 0
        r = 0

        t_counts = {}
        for c in t:
            if c in t_counts:
                t_counts[c] = t_counts[c] + 1
            else:
                t_counts[c] = 1

        def is_sub(s: str, t: str) -> bool:
            if len(t) > len(s):
                return False
            
            t_counts_copy = t_counts.copy()
            
            for c in s:
                if c in t_counts_copy:
                    t_counts_copy[c] = t_counts_copy[c] - 1
                    if t_counts_copy[c] == 0:
                        del t_counts_copy[c]    

            return len(t_counts_copy) == 0

        best = ""
        while r <= len(s) - 1:
            sub = s[l:r+1]
            # print(sub)
            # print(len(sub))
            # print(len(t))
            if is_sub(sub, t) and len(sub) >= len(t):
                if best == "":
                    best = sub
                elif len(best) > len(sub):
                    best = sub
                l += 1
            else:
                r += 1

        return best

            
