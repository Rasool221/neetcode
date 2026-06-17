# okay i mean this is a simple problem description, no room for misunderstandings i think
# i think iterating from left to right i can take that number and then iterate from right to left from that number 
# to the beginning of the array, looking for nums smaller than the last smaller number, and keeping track of a global counter
# problem states o(n^2) is acceptable for space and time but i think my solution is O(N^2) in time but O(1) in space
# i think i also need to get rid of dupe numbers in the input list since they will be counted with my approach
# we can either skip dupes during processing or just dedupe the input list
# this brings space complexity up to O(n) (processing from last element backwards) but still within problem range

# [0,1,0,3,2,3] this input breaks it
# because my solution counts the 0 after the 1 then doesnt count the 0
# so clearly im not implementing a valid solution, my solution is greedy, not a dp solution
# let me think of a recurrance relation that works here
# what if we build a dp array by scanning left to right on the input nums array
# such taht every element in the dp array represents how many sequences can be formed on that path
# then to compute the subsequences at index i we just look back at other calculated elements
# and count upwards from previous stored values
# recurrance relation is something like:
# dp[i] = max(dp[j] + 1, dp[i]) for j < i if nums[j] < nums[i]
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        # dp[0] = 1 # only 1 subsequences at index 1 of nums
        
        for i in range(1, len(nums)):
            for j in range(i+1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i]) # extend the largest of previous subsequences


        # return longest LIS
        return max(dp)
        


