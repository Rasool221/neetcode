class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1 # this is O(1)!

        # nums1 is now always the smaller array

        total_len = len(nums1) + len(nums2)
        half = total_len // 2

        # for binary searching the smaller arr
        l = 0 # left bound for bin search
        r = len(nums1) - 1 # right bound for bin search
        while True:
            lp = (l + r) // 2 # left partition index
            rp = half - lp - 2 # right partition index

            # if out of bounds we go to + or - infinity
            if lp >= 0:
                ll = nums1[lp]
            else:
                ll = float('-infinity')

            if lp + 1 < len(nums1):
                lr = nums1[lp  + 1]
            else:
                lr = float('infinity')

            if rp >= 0:
                rl = nums2[rp]
            else:
                rl = float('-infinity')

            if rp + 1 < len(nums2):
                rr = nums2[rp + 1]
            else:
                rr = float('infinity')

            # partitions are correct
            if ll <= rr and rl <= lr:
                # median is same value, return whichever is not out of bounds
                if total_len % 2:
                    return min(lr, rr) 
                
                # median is avg of 2 middle values that arent out of bounds
                return (max(ll, rl) + min(lr, rr)) / 2 
            elif ll > rr:
                r = lp - 1 # decrease partition size
            else:
                l = lp + 1 # increase partition size

        



        
