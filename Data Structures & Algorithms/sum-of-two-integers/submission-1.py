# let's see, binary representation of 1, and 2 is 0010
# for the first example 1 + 1 = 2, we can take 0001 + 0001 = 0010, obviously without using +
# so lets think of some bitmask operations that would help us here.
# let's show the other example 4+7=11
# 4 = 0010, 6 = 0100, 11 = 1011

# so we can sum a and b using XOR, then calculate carry using AND
# whicih can give us a carry value, then we sum them again until carry (second number) is 0

# nice this works for summing positive numbers, but does not work for summing negative
# numbers or positive & negative numbers

# hmm, how would we do that
# first, we dont step when carry is over 0, we stop when it is non-zero
# second, we can check the sign first bit and if its negative, we work to make it positive by subtracing 2^32 (this is a python quirk from what i can tell, other languages handle this better, python just makes all ints infinitely large)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF # all 1s, helps us cap to 32 bit size bc Python doesn't use 32 bit registers

        while b != 0:
            sum_ = (a ^ b) & MASK # a XOR b gives us the sum without carry
            carry = ((a & b) << 1) & MASK # a & b generates the carry positions, and shift to left as to move them forward

            # we're going to need to add carry to sum until carry is 0, so we keep going 
            # by resetting these values to our calculated sum and carry
            a = sum_ 
            b = carry
        
        # now we can check if a has the sign bit set, indicating its negative but python
        # isn't interpreting it as such (because Python wants to have infinite expanding ints, not 32 bits)
        SIGN_BIT = 1 << 31 # the check bit
        INT_MOD = 1 << 32 # 2^32, subtracting by this will fix Python's interpretation as a negative number
        if (a & SIGN_BIT) != 0: 
            a -= INT_MOD 

        # a eventually will be the total sum
        # so we can just return that 
        return a

