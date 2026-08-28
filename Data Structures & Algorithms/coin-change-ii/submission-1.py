class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # nice edgecase guys
        if amount == 0:
            return 1

        # 2d grid of coins on x axis, 1..amount on y axis
        g = []

        # creating the grid
        for _ in range(amount):
            g.append([0] * len(coins))

        # populating grid
        for j in range(len(g)):
            a = j + 1 # the current amount
            for k in range(len(g[j])):
                # the coin used for the calculation later
                c = coins[k] 

                # if count greater than amount and we have a prev # value, we simply just carry it over. if no prev # value we just keep it as 0
                # the simple rule is, carry previous value 
                # and add amount of times to make leftover 
                # if the current coin is <= amount
                # if no prev value, just insert 1 if coin <= amount
                # essentially:
                # (prev coin) + (ways to make coin - amount) if count <= amount

                w = 0 # amount of ways for cell

                # carry prev coin if one is available
                if k > 0:
                    w += g[j][k - 1]

                # keep this in case there is a remainder
                remainder = a - c 

                # current coin 
                if remainder > 0:
                    w += g[remainder - 1][k]
                elif remainder == 0:
                    w += 1

                g[j][k] = w
        
        # debug
        # for r in g:
        #     print(r)

        return g[-1][-1]

        