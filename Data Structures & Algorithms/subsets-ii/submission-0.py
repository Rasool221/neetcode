class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answers = []
        nums.sort()

        def recurse(i: int, s: list[int]):
            nonlocal answers
            
            if i >= len(nums):
                answers.append(s)
                return

            n = nums[i]
            if i < len(nums) - 1:
                print(f"{i=} {nums=} {n=} {nums[i + 1]=}")
            while i < len(nums) - 1 and nums[i + 1] == n:
                print(f"{i=} {n=}")
                i += 1

            print(f"{i=} {nums=} {n=}")

            recurse(i + 1, s + [n])
            recurse(i + 1, s)

        recurse(0, [])
        return answers