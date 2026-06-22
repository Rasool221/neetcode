# honestly, ive only read the question once and i think i understand
# but i think my initial thought to solve this is a bit too stupid
# which is to just take a max of all triplet positions of all triplets and see if that matches target?
# unless target doesnt always represent the largest values of all triplets, which is probably the case
# however not mentionee explicitly or a sample test case exists
# i want to try it out just to rule out this ambigiouity 

# ok as expected that stupid idea didnt work because the 3rd test case was 
# [[2,5,3],[1,8,4],[1,7,5]]
# [2,7,5]

# now i think what i want to do is scan linearly through triplets, keep a current running triplet
# and keep an eye on target, and depending on relative values of ai, bi, ci and at, bt, ct, we should 
# be able to see if our running triplet == target at the end
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = [triplets[0][0], triplets[0][1], triplets[0][2]]

        for triplet in triplets:
            for i in range(3):
                if target[i] > cur[i] and triplet[i] <= target[i]:
                    cur[i] = max(triplet[i], cur[i])

        # print(cur)

        return cur == target