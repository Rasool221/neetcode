class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_raw = t
        t = set(list(t))
        l = 0
        r = 0

        best = ""
        while r <= len(s) - 1:
            sub_raw = s[l:r+1]
            sub = set(list(s[l:r+1]))
            # print(sub)
            # print(len(sub))
            # print(len(t))
            if t <= sub and len(sub) >= len(t_raw):
                if best == "":
                    best = sub_raw
                elif len(best) > len(sub):
                    best = sub_raw
                l += 1
            else:
                r += 1

        return best

            
