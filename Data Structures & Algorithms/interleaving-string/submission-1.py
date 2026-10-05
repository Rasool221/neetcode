# so i think using recursion we can model the problem well
# however the only confusing bit is that in the case 
# where we have ambigious substrings. for example, in my implementation
# im iterating 1 character at a time on t3, and if we can make potential substrings
# from both s1 & s2 because they share the same char.

# ah, we actually dont care about the ambigiouity case
# because with caching added on the solve function and 
# the branching mechanics of recursion we will test all possible paths
from functools import cache 
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # since our base case earlier depends on len(s3) = len(s1) + len(s2) and since
        # that makes since towards the structure of the problem, we will add that as a
        # base case here
        if len(s1) + len(s2) != len(s3):
            return False
        
        @cache
        def solve(n: int, m: int) -> bool:
            # base case, reaching past the end means 
            # the interleaving happens
            if n + m >= len(s3):
                return True

            # the current index of s3 can be derived
            # from n + m
            c = s3[n + m]

            # since we can potentially be out of bounds for both
            # current index of s1 and s2, we can use None so checks
            # below can work as intended while ignoring the branch with the 
            # string we've ran out of chars with
            sc = s1[n] if n <= len(s1) - 1 else None
            tc = s2[m] if m <= len(s2) - 1 else None

            if c == sc and c == tc:
                return solve(n + 1, m) or solve(n, m + 1)
            elif c == sc:
                return solve(n + 1, m)
            elif c == tc:
                return solve(n, m + 1)

            # if we cannot match current char
            # to anything, we collapse this branch
            return False


        return solve(0, 0)