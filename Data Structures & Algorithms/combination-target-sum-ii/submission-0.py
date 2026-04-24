class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answers = []

        seen = set()

        def recurse(so_far: List[int], i: int):
            nonlocal answers
            nonlocal seen

            so_far_identifier = tuple(so_far)           

            if so_far_identifier in seen:
                return

            sum_so_far = sum(so_far)
            if sum_so_far == target:
                answers.append(so_far)
                seen.add(so_far_identifier)
                return
                
            if sum_so_far > target:
                return

            if i >= len(candidates):
                return

            n = candidates[i]

            recurse(so_far, i + 1)
            recurse(sorted(so_far + [n]), i + 1)

        recurse([], 0)
        return answers

        