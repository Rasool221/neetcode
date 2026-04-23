class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answers = []

        def recurse(so_far: int, i: int): 
            nonlocal answers

            if i >= len(nums):
                return 

            sum_so_far = sum(so_far)
            if sum_so_far == target:
                answers.append(so_far)
                # if we've reached the target, no reason to keep going
                # a larger sum would go over the target
                return 

            n = nums[i]

            if n + sum_so_far > target:
                return

            # add with self, stay on self
            recurse([n] + so_far, i)

            # add with self, move to next
            # recurse(so_far, i + 1)

            # move to next
            recurse(so_far, i + 1)

        recurse([], 0)
        return answers
        
