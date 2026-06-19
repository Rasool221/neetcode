# i think this is a bit tricky but simple
# i think its just like jump game 1 where you take the max
# of current jump amount and amount remaining,
# but also the destination of either remaining jumps or current jump
# and take max of those as well 

# actually i think im just being stupid, im trying to think of a case
# that wouldnt work with the jump game 1 solution, which i think this one 
# is basically the same problem but instead we count the amount of jumps we make
# instead of returning true/false

# let's see, i think because our goal is to reduce amount of jumps we're making
# i think thats basically the last solution??

# ah its almost like, when we scan linearly and have a jump we can make
# we can scan all of the spots between and find which one boosts us the furthest before reaching dest

# here's a case we need to make sure we have nailed down
# [1,4,5,6,9,7,0,0,0,0,0,0,0,0]
# the thing is 4 can take us to 7, but we miss the 9 between
# so as we scan linearly to get from 4 to 7, we need to make sure
# we pick 9. 

# ah in jump game 1 we take first route greedily, because any would work for the answer
# in this one we need to make sure we take the least in O(n) time. 
class Solution:
    def jump(self, nums: List[int]) -> int:
        # no jumps needed to reach last element
        # if only 1 element exists
        if len(nums) == 1:
            return 0

        jumps = 1 # starting at 1 jump because we wont count last one 
        i = 0 # where we currently are

        # if we reached the last element that means 
        # we can return amount of jumps, we dont to actually reach it
        while i < len(nums) - 1:
            n = nums[i]

            next_index = i + n

            # scan through places in between, taking 
            # the max distance between all of them as our next jump
            for j in range(i, i + n):
                next_index = max(next_index, nums[j] + n)               

            i = next_index
            jumps += 1

        return jumps