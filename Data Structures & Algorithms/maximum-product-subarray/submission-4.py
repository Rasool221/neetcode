# so this problem is pretty clear, we just return the max 
# product subarray. contigous is important and makes this problem easier 
# i think. one thing i am not sure about immediately are negative numbers, my intuition
# is telling me to filter them out as they wont contribute to a large product, however
# if the input array was all negative numbers, we still need to find the max subarray, so we cant filter
# them out. however, if we have a positive number that we've considered part of our subarray, we shouldnt try negative numbers
# and reset.

# i actually dont think that mental model about resetting works because it feels like im reaching for some kind 
# of backtracking solution when i should just focus on dp here

# in that case, i will just treat negative numbers as normal

# actually, we need to track negative numbers, because if we have a running product that's negative, multiplying by 
# another negative number actually gives us a positive number that's larger, making that subarray valid

# let me try to do a bottom approach, that seems easier to think about since this is max style arithmetic
# i think ill track answer globally but use bottoms up dp list to track current max product subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        dp[0] = nums[0] # set dp arr to first element, standard for bottom up dp
        answer = nums[0] # init answer to first element, for inputs with 1 element

        for i in range(1, len(nums)):
            n = nums[i]
            
            # either reset the contigious
            # product, or keep going
            dp[i] = max(n * dp[i - 1], n)

            # compare every step against the global max
            answer = max(dp[i], answer)

        # print(dp)
        return answer
