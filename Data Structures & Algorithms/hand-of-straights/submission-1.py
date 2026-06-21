# okay so we try to break up hand into consecutive groups
# of size groupSize. may or may not be possible, we just return if it
# is or isnt, so we may not actually need to create the groups

# what's stopping us from just sorting the array and calculating manually?
# that seems easy enough right?

# the problem is that then the array that includes duplicate numbers
# puts dupe numbers together: 
# before: [1,2,4,2,3,5,3,4]
# after: [1,2,2,3,3,4,4,5] -> [1,2,3,4] [2,3,4,5]

# maybe now get min, max, iterate over that, and keep a frequency hash map of 
# values, which we iterate forwards, counting groups as we take away from frequency map,
# then process whether we can do this or not

# i think we can also safely return false if you cannot divide groupSize evenly into 
# the list. its not a true determination, however it will weed out some invalid inputs cleanly

# the question is can we process the frequency map in one linear scan from beginning to end of
# min and max n? or do we need a while loop that may take longer than O(n)

# let's think of the freq map for that example
# {1: 1, 2: 2, 3: 2, 4: 2, 5: 1}

# what if we buckets[i] where i is ith hand and buckets[i] is the last number in that hand
# that way when we iterate from min_n to max_n and count how many cards in our freq map
# we can spread out that number across buckets up to groupSize amount
# example:
# [1,] <- appears only once
# [2, 2] <- 2 appears twice, update the one and add a new two
# [3, 3] <- 3 appears twice, update both since its their next consecutive number
# [4, 4] <- 4 appears twice, update both
# [5, 4] <- 5 appears once

# actually i can just keep track of the entire sequence, since at most they will make n items,
# so O(n) space
# i will need to keep track of the entire sequence because it will help determine whether this was valid
# or maybe we dont actually need to keep track of the entire sequence, if our len(buckets) == len(hand) // groupSize

# actually one more thing missing, i need to check that we've built buckets of the correct groupSize length
# so ill modify my buckets array  to store a tuple, the last sequence number and the length, then we can simply check
# at the end that all lengths are as expected (groupSize)
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize > len(hand):
            return False

        # not a perfect indicator but still helpful
        if len(hand) % groupSize != 0:
            return False

        hand.sort()

        min_n = float('inf')
        max_n = float('-inf')

        # n -> amt it appears in hand
        freq = {}

        # getting min and max n,
        # then counting the occurances of n
        for n in hand:
            min_n = min(n, min_n)
            max_n = max(n, max_n)
            
            freq[n] = freq.get(n, 0) + 1

        # buckets[i] = (last sequence #, length of bucket)
        buckets: tuple[int, int] = []

        for i in range(min_n, max_n + 1):
            if i not in freq:
                continue

            for j in range(len(buckets)):
                s, l = buckets[j]

                # if we can extend hand at j
                if s == i - 1 and freq[i] > 0 and l < groupSize:
                    buckets[j] = (i, l + 1) # set last hand and increment
                    freq[i] -= 1 # subtract from frequency map

            # now if we still have some m left over here
            # that means we can just add them to start a new bucket
            while freq[i] > 0:
                buckets.append((i, 1))
                freq[i] -= 1

        # now checking if we built buckets correctly
        return all(length == groupSize for _, length in buckets)
