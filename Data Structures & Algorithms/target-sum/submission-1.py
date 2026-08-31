"""
haven't been feeling my sharpest lately. 
let's do this top-down using recursion,
and I will explore the bottom up solution later
"""
from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # top down func till take 2 params:
        # - current index in array
        # - current sum
        # we will iterate the array by increasing index
        # and we will perturb the sum plus/minus current index
        # when we reach the end, we will check if we've reached target
        # thus we will return the amount of ways to reach solution
        @cache
        def solve(i: int, cur_sum: int) -> int:
            if i > len(nums) - 1:
                if cur_sum == target:
                    return 1
                else:
                    return 0
            
            n = nums[i]
            return solve(i + 1, cur_sum + n) + solve(i + 1, cur_sum - n)

        return solve(0, 0)
        