# [1,2,3]
# [[1], [2,3], [2], [1,3], [3], [1,2], [1,2,3], []]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answers = []
        if len(nums) == 0:
            return []

        answers.append([])

        for n in nums:
            answers.append([n])
            exclusive_subset = [c for c in nums if c != n]
            if len(exclusive_subset) > 1:
                answers.append(exclusive_subset)

        if len(nums) > 1:
            answers.append(nums)

        print(f"{answers=} {type(answers)}")
        return answers