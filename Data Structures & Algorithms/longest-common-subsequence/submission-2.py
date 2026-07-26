"""
text1 = "cat", text2 = "crabt"

   c  r  a  b  t
c [0, 0, 0, 0, 0],
a [0, 0, 0, 0, 0],
t [0, 0, 0, 0, 0],

The idea is to keep a 2d array of integers, and 
process bottom up if the amount of the longest
common subsequence

Then we go column by column downwards and looking
extending the # of LCS from top or left. The reason
for top or left. 

Then the answer is going to the bottom right cell
which is the LCS of both words completely.

   j  m  j  k  b  k  j  k  v
b [0, 0, 0, 0, 1, 1, 1, 1, 1]
s [0, 0, 0, 0, 1, 1, 1, 1, 1]
b [0, 0, 0, 0, 2, 2, 2, 2, 2]
i [0, 0, 0, 0, 2, 2, 2, 2, 2]
n [0, 0, 0, 0, 2, 2, 2, 2, 2]
i [0, 0, 0, 0, 2, 2, 2, 2, 2]
n [0, 0, 0, 0, 2, 2, 2, 2, 2]
m [0, 1, 1, 1, 2, 2, 2, 2, 2]

This test case is now failing, and it's because 
I am double counting b as LCS twice in one column, although 1 pair 
should be counted only once per column. I can fix that via a set.

"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # text1 will be larger or the same as text2
        # text1 will also be the width always
        text1, text2 = (text1, text2) if len(text1) > len(text2) else (text2, text1)
        w, h = len(text1), len(text2)

        dp = []

        # seeding the table
        for i in range(h):
            dp.append([0] * w)

        # print(f"{text1=} {text2=} {w=} {h=}")

        # going through the table
        for i in range(w):
            paired = set()
            for j in range(h):
                t1 = text1[i]
                t2 = text2[j]               

                potential = 0
                up = dp[j - 1][i] if j > 0 else 0
                left = dp[j][i - 1] if i > 0 else 0

                # if we found a letter pair, we 
                # need to only count it once, otherwise 
                # we may count an LCS=2 when text1 = "b" and text2 = "bb"
                if t1 == t2 and t1 not in paired:
                    potential = 1
                    paired.add(t1)

                # pick the max out of the following options:
                # - value left of cell if can reach
                # - value on top of cell if can reach
                # - above values + 1 if t1 == t2
                dp[j][i] = max(
                    up,
                    left,
                    potential + up,
                    potential + left,
                )

        # for i in range(len(dp)):
        #     print(dp[i])

        return dp[-1][-1]