# aside from the utter confusion of "encode" string -> digits, this problem
# is "decoding" a string INTO digits or rather returning how many possible decodings there
# are, AND the string being actually numbers...this problem is interesting
# we are given a string of numbers, and we are to output how many different ways it can be 
# turned into letters.
# context: A -> 1, B -> 2... Z -> 26
# input: s = "12", output: 2, "12" can be decoded as "AB" (1 2) or "L" (12)
# input: s = "01", output: 0, because 01 is not a valid letter
# important thing to note is that for any number >= 2 && <= 26 it can be mapped to a single letter
# OR multiple letters. however, if its >26 it has to be broken down

# i think we iterate from left to right, attempting to look at the next element to make a letter
# as long as the number <= 26 (combined), we can make on letter.
# in that case, we branch off in 2 paths. take 1 letter only, or attempt to take the second letter
# if the current number is 0, we dont attempt to take next

# ok were at 7/27 passing now, failing at this test case
# s="10", expected output: 1, actual output: 2.
# its because of the second 0, where im moving to next char
# after processing 1 optimistically, but the next char isnt a letter, so we cant add "A" as an
# answer if the next number is 0, we can only join them. therefore, I will only add invidiual n
# to the answer iff next n isn't 0

# ok im getting TLE on test case 25/27, clearly this is too much of a brute-force solution although it works
# let's do this, instead of solve computing all possible answers and adding to a global array,
# we instead make solve compute the amount of interpretations that can be made for rest of string

# in that case here's what we do:
# - if cur number is 0, we simply just move on
# - if next number is 0, we can only count cur number + next number if <= 26
# - if we're at the last element, we can onl

from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        answers = []

        if len(s) == 0:
            return 0

        if s[0] == "0":
            return 0

        # i represents the index of string s,
        # returns # of interpretations from s[i:]
        @cache
        def solve(i: int) -> int:
            # if we're at the last element or surpassed
            # last element, we can count it
            if i == len(s):
                return 1

            # now, we recurse on only taking the current n at index i
            # and then we look ahead 1 char, if its <= 26 together with current one, we 
            n = s[i]

            if n == "0":
                return 0

            # 1 digit bite
            ways = solve(i + 1) 
            # 2 digit bite when we can
            if i + 1 < len(s) and int(n + s[i + 1]) <= 26:
                ways += solve(i + 2)                 

            return ways

        return solve(0)