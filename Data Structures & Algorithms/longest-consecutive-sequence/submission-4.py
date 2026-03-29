# approach
# [2, 20, 4, 10, 3, 4, 5]
# turn into set {2, 20, 4, 10, 3, 4, 5}
# if beginning of sequence
    # count up until sequence breaks
    # keep track of longest seq
# return longest sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        longest = 0
        for i in range(len(nums)):
            n = nums[i]
            cur = n
            if n - 1 not in seq:
                cur_len = 0
                while cur in seq:
                    cur_len += 1
                    cur += 1

                if cur_len > longest:
                    longest = cur_len

            seq.add(n)
        
        return longest