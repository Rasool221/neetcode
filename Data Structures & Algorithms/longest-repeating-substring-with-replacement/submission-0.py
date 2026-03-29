# expand window when length of most common - window size <= k
# keep track of most common char
# keep track of all chars in hashmap, at each iteration, enter it
# length of map = # of unique characters
# r - l + 1 = window size
# length of most common = max(map.values()) which is O(26) so still o(n)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        w = {}
        gmax = 0
        for r in range(len(s)):
            c = s[r]

            # keep track of chars
            w[c] = w.get(c, 0) + 1
            w_size = (r - l) + 1
            mcc = max(w.values())

            # print(w_size, mcc)

            # invalid window
            while w_size - mcc > k:
                # remove l from w
                lc = s[l]
                w[lc] = w[lc] - 1
                if w[lc] == 0:
                    del w[lc]
                l += 1
                w_size = (r - l) + 1
            
            # print(l, r, w)
            gmax = max(w_size, gmax)

        return gmax

            
            




