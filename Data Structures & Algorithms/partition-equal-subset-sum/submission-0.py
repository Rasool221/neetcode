# hmm let's try to formulate some kind of recursion, or some smaller
# problem to solve, one thing to note is problem is unclear whether
# the input list is sorted or not, however i dont think it matters too much for us
# alright what's the smallest subproblem?
# a list with one number [1] cannot be broken down into two subsets 
# the list [1,2] cannot be broken down into two subsets
# the list [1,2,3] can be broken down, [1,2] and [3]

# let's say we have [1,2,3], and we're iterating from left to right
# let's say at each step we want to add the current number to either the left bucket or the right bucket, both initially start at 0
# left: 0, right: 0, n=1
# left: [1], right: 0, n=2
# left: [1], right: [2], n=3 where do we place 3? maybe we need some kind of balancing technique
# left: [1,2], right: [3] search left for the difference 

# let's run through [1,2,3,4]
# left: 0, right: 0, n = 1
# left: [1], right: 0, n=2
# left: [1], right: [2], n=3 n>=sum(right) so we pop right and move left?
# left: [1,2], right: [3] n=4
# no i dont think this works, i think im reach for a heap based approach

# let's go back to thinking in terms of recurrance relations:
# [1,2] cant have equal subset sums, because the sum is 3 and you cant break down 3 in half using only integers, thus 
# we can eliminate all odd sum nums arr

# alright, so [1,2,3] can be broken down into [1,2] and [3]
# the total sum of [1,2,3] is 6, so we try to find 2 subsets that equal to 6/2
# so what if we recursively try to find a subset that sums to a target
# and if one subset is found, that means another one can be found as well 

# with tihs new approach, let's try [1,2,3,4]
# total sum is 10 which is even so it can be split into subsets of each summing to 5
# therefore, we try to find one subset that can sum to 5, and if we can find it, we can return true
# we can do this with recursion, by either taking the current number if it + sum_so_far doesnt exceed target or not taking the element at all

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # odd nums sum cannot be broken down into equal halves using ints only
        if sum(nums) % 2 != 0:
            return False

        # our target is to find a subset that can make half of sum of nums list
        target = sum(nums) // 2

        # i is in the index of nums we're on
        # so_far is the sum of elements so far in this tree
        # returns whether we can find a subset or not for target
        def solve(i: int, so_far: int) -> bool:
            # base case, we've exceeded nums arr
            if i >= len(nums):
                return False

            # base case, we've found a subset
            if so_far == target:
                return True

            n = nums[i]
            
            found = False

            # branch one, if adding current number doesnt exceed target, go down that route
            if so_far + n <= target:
                found = solve(i + 1, so_far + n)

            # branch two, dont add current element, should find other cases where current element
            # isnt apart of the subset
            found = found or solve(i + 1, so_far)

            return found

        return solve(0, 0)