# i think i just take the max of the current element
# and the next element and jump that amount, as long as current element isnt 0?
# test case 1 is pretty straightforward, let me look at case 2 closer
# [1,2,1,0,1] so if you take either index 1 or 2, you cannot make it to the last index
# what if it was [1,2,3,0,1] you would be on index 1, looking an element ahead,
# then you would just go to index 2, and take that jump, this is why i think you need to look ahead
# now the question is do you look behind as well and take the max of all?
# [5,2,3,0,1] if this was the case, then i think yes, hm but wait thats just looking ahead
# when you're at index 0 & looking behind doesnt make sense because that's already in the past
# ok i tried to get fancy with the while loop and dynamic jumping
# which got me 25/32 test cases, but this one makes it clear that i need a linear scan 
# with a simple counter i think
# [3,0,8,2,0,0,1] because i get trapped at 2 and miss the 8
# 
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        c = nums[0]

        # if we only have 1 element, we're already at the end
        if len(nums) == 1:
            return True
        
        for i in range(len(nums)):
            n = nums[i]

            # if we land exactly at the last element, we're good
            if i == len(nums) - 1:
                return True

            # if we're out of jumps and we cant jump anymore we're cooked
            if c == 0 and n == 0:
                return False

            # set the amount of jumps remaining to 
            # max(jumps remaining, current jump amount)
            c = max(n, c)
            
            # take 1 jump
            c -= 1 

        return True
