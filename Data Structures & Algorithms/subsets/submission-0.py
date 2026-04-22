class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answers = []
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [[nums[0]], []]

        answers.append([])

        def recurse(num: int): 
            answer = []
            for n in nums:
                if n == num:
                    continue
                answer.append(n)

            nonlocal answers
            answers.append(answer)

        for n in nums:
            answers.append([n])
            recurse(n)

        answers.append(nums)
        return answers