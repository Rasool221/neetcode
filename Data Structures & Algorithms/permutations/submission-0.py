class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answers = []
        
        def recurse(i: int):
            nonlocal answers
            if i >= len(nums):
                answers.append(nums.copy())
                return

            for i_n in range(i, len(nums)):
                a = nums[i]
                b = nums[i_n]

                nums[i_n] = a
                nums[i] = b

                recurse(i + 1)

                # restoring the nums arr
                nums[i] = a
                nums[i_n] = b
            
        recurse(0)
        return answers