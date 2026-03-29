class Solution:
    def findMin(self, nums: List[int]) -> int:
        lower = 0 
        upper = len(nums)-1
        
        while lower <= upper:
            m = (lower + upper) // 2

            nm = nums[m]
            nm_r = nums[upper]
            nm_l = nums[lower]

            # print(nm_l, nm, nm_r)
    
            if nm <= nm_l and nm <= nm_r:
                return nm

            if nm > nm_r:
                lower = m+1
            else:
                upper = m-1

        return nums[0]



            
