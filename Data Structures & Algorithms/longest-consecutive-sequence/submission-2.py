# approach 1
# 0-3 +3
# 3-2 -1 = 2
# 2-5 +3 = 5
# 5-4 -1 = 4
# 4-6 +2 = 6
# 6-1 -5 = 1

# approach 2
# min = 2, max = 2, seen = {2}
# min = 2, max = 20, seen = {2, 20}, cur_index = 1, len(nums) - 1 = 6, digits_left = 5, diff = 18 > digits_left skip number

# approach 2
# min = 0, max = 0, seen = {0}
# min = 0, max = 3, seen = {0,3}
# min = 0, max = 3, seen = {0,2,3}

# plan
# keep seen set, if number is seen already, continue
# if diff > digits_left, continue
# enter rest of items in another array
# bucket sort the array o(n)
# return largest sequence without a gap

# negative numbers kills this plan
# should have been a clarification question!!! 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set()
        seq_arr = []
        max_so_far = 0
        min_so_far = 0
        for i in range(len(nums)):
            n = nums[i]
            
            if n in seq:
                continue

            if n > max_so_far:
                diff = abs(n - max_so_far) - 1
                digits_left = (len(nums) - 1) - i

                if diff > digits_left:
                    continue                    

            if n > max_so_far:
                max_so_far = n

            if n < min_so_far:
                min_so_far = n

            seq_arr.append(n)
            seq.add(n)

        # bucket sort
        offset = abs(min_so_far)
        sorted_arr = ["."] * (max_so_far + offset + 1)
        for i in seq_arr:
            i_offset = i + offset
            sorted_arr[i_offset] = i

        largest_seq = 0
        cur_seq = 0
        for i in sorted_arr:
            if i != ".":
                cur_seq += 1
                if cur_seq > largest_seq:
                    largest_seq = cur_seq
            else:
                cur_seq = 0

        return largest_seq

        