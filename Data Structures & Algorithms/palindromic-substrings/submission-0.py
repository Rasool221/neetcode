# trying to find the right subproblem to choose here to solve for
# but i think at the very least, each letter is a palindrome, so that is one 
# of our base cases, if the len(s) == 1 then we return 1

# my intuition so far is reaching for all sorts of iterative solutions, but
# that doesn't really solve this problem. it may fit the 2 example test cases "abc" and "aaa"
# however, what about this test case? "aracecarb", 
# where the output is len("aracecarb") + 1 (the "racecar" substring being a palindrome)

# so i need to find a way to capture that as well with this dp solution

# i need some branching strategy that separates the string into substrings deep enough into single chars
# where the lower bound will at least be given (len(s))

# to help guide my thinking here are some cases where my initial approaches dont work:
# "abracecarabc"

# let me try re-doing my longest palindromic substring solution here and modifying it, it has to be 
# the same problem, right? we're looking for palindromic substrings but instead of getting the longest,
# we're just counting. conceptually, we start iterating from left to right of the string, then attempt 
# to treat that point as a midpoint of a palindome, expand leftwards and rightwards. if what we're looking at 
# is a substring, add the total, otherwise keep going. 

# what i described above is the odd case where the palindrome is an odd number of chars
# for even number of chars (no single midpoint), we expand from current position and next position, and 
# because were iterating from left to right on the given string, we treat the center as 2 chars, counting even number
# paldinromic strings appropriately
class Solution:
    def countSubstrings(self, s: str) -> int:
        m = 0 # m for middle

        total = 0

        # this function takes in the input string,
        # initial starting points of left and right locations
        # and returns the # of palindromic substrings found
        def expand(s: str, l: int, r: int) -> int:
            # if we're exceeding the string's bounds we dont need to
            # expand from there, it will cause a duplicate count.
            if r > len(s) - 1:
                return 0

            amount = 0

            while l >= 0 and r < len(s) and s[r] == s[l]:
                p = s[l:r+1]

                # count the palindromic string os far
                amount += 1               

                l -= 1 # expand left
                r += 1 # expand right

            return amount

        for i in range(len(s)):
            total += expand(s, i, i) # expand from center where center is odd in middle of palindrome
            total += expand(s, i, i + 1) # expand from center where center is even in middle of palindrome

        return total 
