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

# ok so thsi approach works naively for 15/28 test cases,
# howver it fails for the folllowing test case: [-2,3,-4] because we're only comparing step by step rather than a running count
# we output 3 instead of -2*3*-4=24
# hmm how do we solve this. 
# maybe we keep a global max thus far, that is either reset or kept moving, almost like a crossover between kadanes alg (but for products) and dp
# ah okay looking at hint we also need to keep a min as well as a max (so far), that makes sense, because ultimately the answer is either 
# - n * max_so_far (current num contributes to product),
# - n (by itself, resetting)
# - n * min_so_far (current num is negative and contributes to max product)
# in that case, we dont even need to keep a dp array

# this problem is actually difficult, thankful for the hints lol
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = nums[0] # init answer to first element, for inputs with 1 element
        max_so_far = nums[0] # init to first num
        min_so_far = nums[0] # init to first num

        for i in range(1, len(nums)):
            n = nums[i]
            
            max_temp = max_so_far

            # computing max_so_far
            # more explanation in above comments
            max_so_far = max(
                n * max_so_far,
                n,
                n * min_so_far
            )

            # and computing min
            # due to negative numbers this value can be any of the 3 cases
            min_so_far = min(
                n * max_temp, # use max_so_far pre update
                n,
                n * min_so_far
            )

            # answer will always be something in max_so_far
            answer = max(max_so_far, answer)

        return answer
