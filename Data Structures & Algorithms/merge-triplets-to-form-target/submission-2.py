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

# alright, that worked for 11/28 test cases, looks like its failing 
# for this one triplets = [[3,5,1],[10,5,7]], target = [3,5,7]
# so im returning true, when i should actually be returning false. i think this is because
# i am currenty processing a, b, c of the triplets seperately. and when we process separately, we 
# will take max of the 2 other elements, which we must and what we're failing to do right now, because we 
# process a b c seperately. 

# i think that changes the logic in this way: when we're linearly scanning through the triplets,
# if we find a triplet that an a, b, c value that's larget than target, we ignore that triplet entirely
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = [triplets[0][0], triplets[0][1], triplets[0][2]]

        for triplet in triplets:
            # skip triplets that have any elements exceeding target
            # as they will not give us a valid answer because we have to take
            # max of all elements
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            for i in range(3):
                # skip if we're already at target
                if cur[i] == target[i]:
                    continue

                # only look to upsize, since problem is clearly max()
                if target[i] > cur[i] and triplet[i] <= target[i]:
                    cur[i] = max(triplet[i], cur[i])

        # print(cur)

        return cur == target