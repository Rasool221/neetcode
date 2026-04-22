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
            answers.append([c for c in nums if c != n])

        answers.append([nums])
        print(answers)
        return answers