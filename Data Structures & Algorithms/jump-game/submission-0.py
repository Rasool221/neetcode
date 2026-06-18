# i think i just take the max of the current element
# and the next element and jump that amount, as long as current element isnt 0?
# test case 1 is pretty straightforward, let me look at case 2 closer
# [1,2,1,0,1] so if you take either index 1 or 2, you cannot make it to the last index
# what if it was [1,2,3,0,1] you would be on index 1, looking an element ahead,
# then you would just go to index 2, and take that jump, this is why i think you need to look ahead
# now the question is do you look behind as well and take the max of all?
# [5,2,3,0,1] if this was the case, then i think yes, hm but wait thats just looking ahead
# when you're at index 0 & looking behind doesnt make sense because that's already in the past
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0

        # we dont need to iterate to the end
        # if we exit out of this loop we dont have a jump path to the end
        while i <= len(nums) - 2:
            n = nums[i]

            # if we can reach the end from here
            if n + i >= len(nums) - 1:
                return True

            # if we've landed on a 0, we cannot continue
            if n == 0:
                break
        
            nn = nums[i + 1]

            # jump the max of current or next - 1
            # since you need 1 jump to reach the next element
            i += max(n, nn - 1)

        return False