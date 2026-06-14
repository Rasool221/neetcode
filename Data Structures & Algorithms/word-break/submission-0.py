# rephrasing this problem: return true if s can be formed from concatenating words from wordDict
# where any word can be re-used any number of times or not used at all
# off the top of my head, im not really sure where to start honestly, but let's try to find some kind of recurrance
# relation, or frame it in some kind of dynamic programming fashion

# im thinking iterating through s and checking wordDict (or some diff data structure containing that data)
# is the right call here, sets us up for a O(n) or close algorithm

# ok so as we are iterating through s, we need to be tracking if we can find that word in wordDict 

# what if we write a fn, called solve(input: str) -> bool which takes in s or a substring of it,
# and returns the same condition as the problem calls for. that way we can split this into multiple subproblems to solve

# for example s = "neetcode", wordDict = ["neet", "code"]
# the callstack will look something like this:
# solve("n") 
#   solve("nee")
#   solve("neet") here we find one word in wordDict, so then we continue iterating through s
#   solve("neetc")
#   solve("neetco")
#   solve("neetcod")
#   solve("neetcode") here we've reached the end of s and havent returned false early, so we return true

# we will also cache the return based on param of the solve fn to avoid re-processing the same values
from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        @cache
        def solve(i: int) -> bool:
            # base case, we've reached the end
            # of s, which also means we found all words
            if i >= len(s):
                return True

            sub = s[i:]

            # if the substring isnt in words,
            # we continue iterating, until
            if s.startswith(sub) and solve(i + len(sub)):
                return True
            else:
                return False

        return solve(0)



