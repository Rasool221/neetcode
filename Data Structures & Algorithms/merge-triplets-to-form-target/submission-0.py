# honestly, ive only read the question once and i think i understand
# but i think my initial thought to solve this is a bit too stupid
# which is to just take a max of all triplet positions of all triplets and see if that matches target?
# unless target doesnt always represent the largest values of all triplets, which is probably the case
# however not mentionee explicitly or a sample test case exists
# i want to try it out just to rule out this ambigiouity 


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        max_a, max_b, max_c = float('-inf'), float('-inf'), float('-inf')
        for a, b, c in triplets:
            max_a = max(a, max_a)
            max_b = max(b, max_b)
            max_c = max(c, max_c)

        return target == [max_a, max_b, max_c]