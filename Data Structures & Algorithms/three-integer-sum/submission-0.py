# [-1, 0, 1, 2, -1, -4]
# sort the array
# [-4 -1, -1, 0, 1, 2]
# iterate one a time, -1 and so forth
    # initialize left ptr = start, right ptr at end
    # left = -4, right = 2
    # check sum, if we're over, move left ptr down and vice versa
    # if we found a triplet, add to answers list
# return answers list

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        added_index = set()
        added_values = set()
        triplets = []

        for i in range(len(nums)):
            n = nums[i]
            l = 0
            r = len(nums) - 1

            while l < r:
                if l == i:
                    l += 1
                    continue

                if r == i:
                    r -= 1
                    continue

                one = nums[i]
                two = nums[l]
                three = nums[r]

                indexes = [i, l, r]
                indexes.sort()
                triples = [one, two, three]
                triples.sort()

                _sum = one+two+three

                if _sum > 0:
                    r -= 1
                    continue
                
                if _sum < 0:
                    l += 1
                    continue

                indexes = tuple(indexes)
                vals = tuple(triples)
                if _sum == 0 and indexes not in added_index and vals not in added_values:
                    added_index.add(indexes)
                    added_values.add(vals)
                    triplets.append(triples)

                l += 1
                r -= 1
            
        return triplets