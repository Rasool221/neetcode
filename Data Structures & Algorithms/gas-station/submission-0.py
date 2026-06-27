# i think one of the cases where we dont have a solution is where sum(cost) > sum(gas), because that would mean
# it costs more than we have gas to complete a circle
# however, i need to think to actually prove that
# well, since the problem calls only moving to the next gas station (without skipping any), then i think my idea is correct

# what if starting from the highest gas and lowest cost station first, and in case of ties preferring the later stations 
# gives us better chances to complete the circuit? that sounds appealing because we would start with the most amount of gas
# that would get us the farthest 
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        best_start = (float('inf'), float('-inf'), 0) # helps us identify where to start
        sum_cost, sum_gas = 0, 0 # helps us identify if we cant make it early on

        # since len(gas) == len(cost), we can do this safely
        for i in range(len(gas)):
            g = gas[i]
            c = cost[i]

            # finding the best starting point with lowest cost and highest
            # gas, favoring stations towards the end of the array
            if c <= best_start[0] and g >= best_start[1]:
                best_start = (c, g, i)

            sum_cost += c
            sum_gas += g

        # check if the cost is more than gas, that means cost is too high and we cant make a circuit
        if sum_cost > sum_gas:
            return -1

        # print(best_start)

        # now i think we just run the simulation
        _, g, end = best_start

        # tracking how many stops we made so we can know when
        # we have made a circuit and break the loop
        stops = 0

        # starting point
        i = end

        # traveling the initial first step first then entering the loop
        while stops != len(gas) - 1:
            fr = i # from station
            to = i + 1 if i + 1 <= len(gas) - 1 else 0 # to station

            # if cost is greater than gas tank, we cant move further
            if cost[to] > g:
                return -1

            # print(g, cost[fr], gas[to], fr, to)

            # new gas = gas tank - old cost + current gas
            g = (g - cost[fr]) + gas[to]

            # print(g)

            i = i + 1 if i + 1 <= len(gas) - 1 else 0 # increment station
            stops += 1 # increment # of stops

        return end
        

        

        

        
        