# this problem is in the dynamic programming section
# however, there's a really reasonable & easy O(n) solution for this using 
# two pointers that i will implement, i think its unnecessary to solve this problem with dp

# the two pointer solution is very simple, we 
# increase right pointer continously at each iteration
# if we have a palindrome between left and right pointer: increase right pointer, dont move left pointer
# otherwise: we move the left pointer to the right pointer
# obv we keep track of the longest palindrome we've encountered

# actually that was an epic fail, it doesnt work
# but i will keep it in out of humility and honesty lol
# i described a bad sliding window solution that doesnt work

# the actual 2 pointer solution involves expanding from outwards
# we pick a center and if we can, we expand to the left and to the right
# as long as that's a palindrome we keep going, if it isnt, we simply move on to the next char

# in the case of "abba" there is no center, so we try both including the next and prev
# char as the center and then keep going or not include it, then compare for best

# at worst, this is an O(N^2) solution but that fits within the requirements of this problem
class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = 0 # m for middle

        longest = ""

        # this function takes in the input string,
        # initial starting points of left and right locations
        # and returns the longest palindromic string found
        def expand(s: str, l: int, r: int) -> str:
            l = max(l, 0)
            r = min(r, len(s) - 1)

            longest = ""

            while l >= 0 and r < len(s) and s[r] == s[l]:
                p = s[l:r+1]
                
                # set longest to current palindrome if 
                # it is longer
                if len(p) > len(longest):
                    longest = s[l:r+1] 

                l -= 1 # expand left
                r += 1 # expand right

            return longest

        for i in range(len(s)):
            longest_odd = expand(s, i, i) # expand from center where center is odd in middle of palindrome
            longest_even = expand(s, i, i + 1) # expand from center where center is even in middle of palindrome

            if len(longest_odd) > len(longest):
                longest = longest_odd

            if len(longest_even) > len(longest):
                longest = longest_even

        return longest 
