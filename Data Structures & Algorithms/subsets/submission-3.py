# [1,2,3]
# [[1], [2,3], [2], [1,3], [3], [1,2], [1,2,3], []]


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answers = []
        if len(nums) == 0:
            return []

        def recurse(i: int, subset: List[int]):
            nonlocal answers
            if i >= len(nums):
                answers.append(subset)
                return

            n = nums[i]
            recurse(i + 1, subset + [n])
            recurse(i + 1, subset)

        recurse(0, [])
        return answers
