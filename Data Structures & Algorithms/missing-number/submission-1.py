# i think we can trivially do this by scanning
# through the list 
# okay well the list isnt always sorted

# i think this is related to the single number question where 
# we create an xor total and then get the max number
# then we iterate from 0 to max number and xor again against the total 
# which should cancel out existing numbers, and the missing should remain
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        t = 0 # xor total
        m = 0 # max of nums

        # first pass, get xor total and max #
        for n in nums:
            t ^= n
            m = max(n, m)

        # second pass, xor the indexes
        # against the total and that should leave the only missing number
        for i in range(m + 1):
            t ^= i

        return t

        