# okay so i was initially confused by this problem but that is cleared up now
# basically we want to make as many substrings as possible such that repearting chars 
# appear in the same substring
# lets think
# what if we keep track of all letters and their positions in the string
# so xyxxyzbzbbisl becomes:
# {x: [0, 2, 3], y: [1, 4], z: [5, 7], b: [6, 8, 9], i: [10], s: [11], l: [12]}
# i think we can play around with this to get our answer, with some kind of interval-merging esq 
# solution
# for example, x spans from 0-3, and y contains 1 which is between range for x, so we "merge" y's interval within
# x's interval
# let's maybe just develop a 2d array like this:
# [[0, 2, 3], [1, 4], [5, 7], [6, 8, 9], [10], [11], [12]]
# now it becomes clearer, we scan linearly through this array, keep a min and max of last sub array, we can decide 
# whether to merge or not, then build an answers array to return post-merge
# this assumes the array we generated is ordered and that's fine, i think naturally it will be sorted
# if we make a dict, since iterating over a dict we get order in the order of insertion which is a linear scan
# of the input string from left to right

# let me make sure this works for the second example:
# abcabc
# {a: [0,3], b: [1,4], c: [2,5]}
# [[0,3], [1,4], [2,5]]
# yeah they overlap backwards from first case but there is an overlap, meaning 
# we would merge all into a size 6 
# im realizing now we dont even need to store all indices of the letter, just a simple min and max would work

# so this idea is working i just need to adjust my answers array, i actually need to maintain the 
# intervals instead of building it quickly, i can get the answers by taking diff of intervals later
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = {} # our char -> [min, max] indices

        # build our index map
        for i in range(len(s)):
            c = s[i]
            if c not in m:
                m[c] = [i, i] # init with min, max
            else:
                m[c][1] = i # or update last index to current one 

        answers = []

        # our span array
        spans = [indexes for indexes in m.values()]

        print(spans)

        # iterate through p and merge these intervals if there's an overlap with the previous interval
        # we start from index 1 because we look behind
        # we will store the results in a new arr which is our answer
        for i in range(1, len(spans)):
            c_min, c_max = spans[i] # current min, max
            l_min, l_max = spans[i - 1] # last min, max

            # if there's an overlap from either side, merge them
            # e.g. [[0, 5], [4, 6]]
            # if there's an overlap add the diffs of the indexes to answers
            # otherwise add their individual diffs seperately
            # furthermore, we need to check if a last answer has been submitted and if 
            # there's an overlap, we need to go back and modify it
            if c_min < l_max:
                if len(answers) > 0:
                    last = answers[-1]
                    answers[-1] = [last[0], max(l_max, c_max)]
                else:
                    answers.append([l_min, c_max]) 
            else:
                # add current one if no overlap
                answers.append([c_min, c_max])

            # print(f"{c_min=}, {c_max=}, {l_min=}, {l_max=}, {answers=}")

        return [(y - x) + 1 for x, y in answers]



