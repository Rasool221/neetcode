class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answers = []
        seen = set()

        def recurse(so_far: List[int], i: int):
            nonlocal answers
            nonlocal seen

            key = (tuple(so_far), i)
            if key in seen:
                return

 #           print(f"{so_far=}, {i=}, {key=}")

            sum_so_far = sum(so_far)
            if sum_so_far == target:
                answers.append(so_far)
                
                return
                
            if sum_so_far > target:
                return

            if i >= len(candidates):
                return

            n = candidates[i]

            recurse(so_far, i + 1)
            recurse(so_far + [n], i + 1)

            seen.add(key)

        recurse([], 0)
        return answers

        