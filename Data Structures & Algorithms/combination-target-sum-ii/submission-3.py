class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answers = []

        candidates.sort()

        def recurse(sum_arr: List[int], sum_int: int, i: int):
            nonlocal answers

            if sum_int == target:
                answers.append(sum_arr)
                return
                
            if sum_int > target:
                return

            if i >= len(candidates):
                return

            n = candidates[i]
            recurse(sum_arr + [n], sum_int + n, i + 1)

            c = i
            while c <= len(candidates) - 1 and candidates[c] == n:
                c += 1

            recurse(sum_arr, sum_int, c)

        recurse([], 0, 0)
        return answers

        