# alright, what would be the recurrance relation here?
# since we're supposed to find the min number of coins to reach amount
# that means at each step we're supposed to use the max coin denomination we have 
# that's <= the current_amount at every step to reach amount
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
            max_coin = max(applicable_coins)

            # subtracting aomunt, returning 1 coin we've used
            # and summing down the callstack for our full answer
            # which will occur after the collapse
            down = solve(amt - max_coin)
            if down == -1:
                return -1

            return down + 1
        
        return solve(amount)

        