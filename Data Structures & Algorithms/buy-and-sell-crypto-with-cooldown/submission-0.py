"""
there is a 1 day cooldown

there are 3 actions:
- buy
- sell
- do nothing

for each action, it puts you into a state:
- buy -> hold
- sell -> sold -> cooldown

so the state graph is roughly:
cooldown:
    - do nothing -> cooldown
    - buy -> hold
hold:
    - do nothing -> hold
    - sell -> sold

sold:
    - cooldown (you can only go to cooldown)

let's say that we have 3 arrays for the 3 states:
- hold[i] - cash on hand at day i
- cooldown[i] - profit at day i 
- sold[i] - profit at day i, day i + 1 is frozen

so given the state graph and the 3 state arrays we've defined, we can derive the following (max() because we're trying to maximize profit):
- hold[i] = max(
                hold[i - 1], # do nothing
                cooldown[i - 1] - prices[i] # buy and hold same day
            )
- cooldown[i] = max(
    cooldown[i - 1], # do nothing
    sold[i - 1], # just sold and now frozen
)
- sold[i] = hold[i - 1] + prices[i] # sold

some thoughts:
- subtract from prices[i] when buying
- add to prices[i] when selling

finally answer would be max(sold[-1], cooldown[-1]) 
because:
- cooldown[-1] can is a catch-all liquidated state, "what if you sold and did nothing on day x"
- sold[-1] "what if you sold on the last day"
- obviously all best states bubble up to last day given our logic
- hold[-1] isn't included because holding at last day would never be better than other 2 states because sitting on unsold shares is always worse

notes:
i needed a ton of help with this problem, and honestly,
it's still not very intuitive. normally, i try to use
offset-based bottom up dp, with i - 1 or i - 2 (like house robber),
however this was my first time translating a state graph into
derivations of different state arrays.
i guess i just need more reps in this space.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # one price or less we cannot sell so 0 profit
        if len(prices) <= 1:
            return 0

        hold = [0] * len(prices)
        sold = [0] * len(prices)
        cooldown = [0] * len(prices)

        # defining base cases
        hold[0] = prices[0] * -1 # buying first always
        sold[0] = 0 # cannot sell on first day
        cooldown[0] = 0 # cooldown on 1st day is impossible so just 0

        for i in range(1, len(prices)):
            hold[i] = max(
                hold[i - 1], # do nothing
                        cooldown[i - 1] - prices[i] # buy and hold same day
                    )
            cooldown[i] = max(
                cooldown[i - 1], # do nothing
                sold[i - 1], # just sold and now frozen
            )
            sold[i] = hold[i - 1] + prices[i] # sold

        return max(cooldown[-1], sold[-1])
        