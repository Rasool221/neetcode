# okay i mean this is a simple problem description, no room for misunderstandings i think
# i think iterating from left to right i can take that number and then iterate from right to left from that number 
# to the beginning of the array, looking for nums smaller than the last smaller number, and keeping track of a global counter
# problem states o(n^2) is acceptable for space and time but i think my solution is O(N^2) in time but O(1) in space
# i think i also need to get rid of dupe numbers in the input list since they will be counted with my approach
# we can either skip dupes during processing or just dedupe the input list
# this brings space complexity up to O(n) (processing from last element backwards) but still within problem range
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        gmax = 0

        # iterate from left to right
        for i in range(len(nums)):
            counter = 0
            last = nums[i]
            seen = set() # to dedupe

            # iterate from i to left
            for j in range(i, -1, -1):
                if nums[j] in seen:
                    continue

                seen.add(nums[j])

                # if we can create a sub sequence
                # add to the counter
                if last >= nums[j]: 
                    counter += 1
                    last = nums[j]

                # print(f"{nums[i]=} {nums[j]=} {i=} {j=}")

            # keep a global max
            gmax = max(gmax, counter)

        return gmax