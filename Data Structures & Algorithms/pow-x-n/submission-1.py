# ok the real challenge here i believe is that i 
# should go for an O(lgn) solution, as other slower
# solutions are trivial

# so lets think about this:
# pow(2, 4) is 2^4 or 2*2*2*2

# what if i break down the problem into smaller
# problems and memoize results? 

# for example pow(2, 4) can be broken down into
# pow(2, 2) * pow(2, 2)
# which maybe can be further broken down into
# pow(2, 1) * pow(2, 1) * pow(2, 1) * pow(2, 1)

# but now im wondering does that even optimize anything
# or just continually break down?

# let me take our earlier example:
# pow(2, 4)
#   pow(2, 2)      *        pow(2, 2)
#   pow(2, 1) * pow(2, 1)   pow(2, 1) * pow(2, 1)

# by the time that pow(2, 2) is caluclated, it is memoized
# and therefore the second pod(2, 2) will pull the 
# cached value 

# so the optimization would work, let's implement this

# one more thing, we need to handle odd n values 
# which we can do by using the % operator and if n
# is odd, we add an extra * pow(x, 1)

# nice that works, but one big gap i forgor about
# are negative exponents. however we can implement this
# easily with the following identity:
# x^-n = 1/x^n

# we can use the same idea as positive n values
# and add a new base case for when n == -1 

from functools import cache
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # the cache decorator here implements this
        # memoization for us
        @cache
        def pow_(x: float, n: int) -> float:
            # base case, x^0 is always 1
            # this path is only reachable if n was 
            # initially passed in as 0
            if n == 0:
                return 1

            # base case, if n == 1, we just return x
            # because x^1 is just x
            if n == 1:
                return x

            # base case but for negative n values
            # which is just inverse
            if n == -1:
                return 1/x

            # now we can take halfs of n, which is safe
            # because if we cannot anymore, we will just use 1
            extra = 1
            if n % 2 != 0:
                extra = pow_(x, 1)

            ans = pow_(x, n // 2) * pow_(x, n // 2) * extra
            # print(f"{x=} {n=} {ans=}")
            return ans

        return pow_(x, n)