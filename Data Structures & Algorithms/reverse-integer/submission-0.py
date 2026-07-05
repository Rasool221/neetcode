# this is interesting, let me think about this:
# i know this is in the bit manipulation section,
# but the clean O(1) time & space solution is just using % and // to extract
# ints 1 by 1, then rebuilding. we will have to check if the int given is outside the signed 32bit int 
# range which we can do easily via comparisons

# now the only logic we need is to handle negative numbers
# so we can just store a bool if the input is negative, and turn
# the output negative
class Solution:
    def reverse(self, x: int) -> int:
        rebuild = 0
        n = x
        is_negative = False

        # treat as positive, and we
        # will turn it negative later
        if x < 0:
            is_negative = True
            n = x * -1

        # we extract the next digit of n,
        # multiply to rebuild it,
        # then move to the next number
        while n > 0:
            k = n % 10 # extract last digit
            rebuild = rebuild * 10 + k # add last digit to rebuild
            n = n // 10 # fully remove last digit to keep going

        # checking if the number overflows 32 bit range, 
        # and if so, return 0 per problem spec
        if rebuild > (1 << 31) or rebuild < -(1 << 31):
            return 0

        return rebuild if not is_negative else rebuild * -1

        
            