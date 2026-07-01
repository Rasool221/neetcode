# i think we can trivially do this by scanning
# through the list 
# okay well the list isnt always sorted

# i think this is related to the single number question where 
# we create an xor total and then get the max number
# then we iterate from 0 to max number and xor again against the total 
# which should cancel out existing numbers, and the missing should remain

# wow the wording is purposefully confusing. n integers in range [0,n], so [0,1] has 2 elements
# and the missing number is 2. what a shameful question. easy fix tho, we dont keep a max, we just use len(nums) + 1.
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        t = 0 # xor total

        # first pass, get xor total and max #
        for n in nums:
            t ^= n

        # second pass, xor the indexes
        # against the total and that should leave the only missing number
        for i in range(len(nums) + 1):
            t ^= i

        return t

        