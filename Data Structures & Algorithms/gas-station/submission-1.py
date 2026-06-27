# i think one of the cases where we dont have a solution is where sum(cost) > sum(gas), because that would mean
# it costs more than we have gas to complete a circle
# however, i need to think to actually prove that
# well, since the problem calls only moving to the next gas station (without skipping any), then i think my idea is correct

# what if starting from the highest gas and lowest cost station first, and in case of ties preferring the later stations 
# gives us better chances to complete the circuit? that sounds appealing because we would start with the most amount of gas
# that would get us the farthest 

# okay this works for 5/24 test cases, now im returning -1 on one that should be valid,
# here are the inputs:
# gas=[5,1,2,3,4]
# cost=[4,4,1,5,1]
# im starting from index 0 (highest gas for lowest cost), but im seeing that its a diff of one
# and if we start from last element, that would get us further most likely.
# so let's adjust our alg to pick best starting point to go off of diff of gas and cost

# okay this is likely not working, let me notice a few more things about this problem:
# - a solution must exist if sum(cost) <= sum(gas)
# - if we fail at station x, we know all previous stations don't work as starting points
# let me adjust my alg with that approach, while doing a simulation going forward from 0
# eventually we return the last valid starting point
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # a solution cannot exist if this is true
        # and a solution HAS to exist if it is false
        if sum(cost) > sum(gas):
            return -1

        start = 0
        current_gas = 0

        for i in range(len(gas)):
            # pump gas at station i, then pay cost to leave it
            current_gas += gas[i] - cost[i]

            # if we cant make it past station i, all stations [0, i] fail
            # so next valid candidate is i + 1
            if current_gas < 0:
                start = i + 1
                current_gas = 0
        
        # the starting point will be the last valid starting point 
        # that we found during our simulation loop
        return start
        

        

        
        