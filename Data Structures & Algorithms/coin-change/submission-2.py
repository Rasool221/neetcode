# alright, what would be the recurrance relation here?
# since we're supposed to find the min number of coins to reach amount
# that means at each step we're supposed to use the max coin denomination we have 
# that's <= the current_amount at every step to reach amount

# ok so that approach works for 26/28 test cases, however im failing on the following:
# coins=[11, 22, 33, 44, 55, 66, 77, 88, 99, 111]
# amount=330
# where i am returning -1 because picking the max coins wil lead down to amt=9 which
# we dont have a small enough coin for. this means we actually need to try all of the coins that 
# are applicable, and pick the min amount of coins returned (i think but that sounds right).  
from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        # cache the responses of solve so we dont re-do same operations
        # many times
        # amt: the current amount, returns amount of coins
        @cache
        def solve(amt: int) -> int:
            # filter to applicable coins
            applicable_coins = [
                coin for coin in coins if coin <= amt
            ]

            # print(f"{amt=} {applicable_coins=}")

            # base case, we've reached the necessary amount
            # returning 0 up the callstack which will sum to our answer
            # we are returning 0 because we used 0 coins
            if amt == 0:
                return 0

            # base case, no applicable coins
            if len(applicable_coins) == 0:
                return -1

            # get the max coin we can apply
            min_coin = float('inf')
            for coin in applicable_coins:
                # the min coin at every coin from applicable conins
                sub = min(solve(amt - coin), min_coin)

                # we dont care about impossible values
                if sub == -1:
                    continue

                # count the min
                min_coin = min(sub, min_coin)

            # now if no branches worked (hence value is still float('inf') from earlier)
            # if so, we dont add 1 to it to return it up the callstack
            if min_coin == float('inf'):
                return -1

            # return up the call stack the min coin at this step +1 coin we just took
            return min_coin + 1
        
        return solve(amount)

        