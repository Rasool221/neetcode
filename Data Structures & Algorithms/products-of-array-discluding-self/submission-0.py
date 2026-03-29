class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []

        for i in range(len(nums)):
            n = nums[i]
            if i == 0:
                prefix.append(n)
                continue
            
            prefix.append(n * prefix[i - 1])
        
        nums_reversed = nums[::-1]
        for i in range(len(nums_reversed)):
            n = nums_reversed[i]
            if i == 0:
                suffix.append(n)
                continue
            
            suffix.append(n * suffix[i - 1])
        suffix = suffix[::-1]
        
        print(nums)
        print(prefix)
        print(suffix)

        ans = []
        for i in range(len(nums)):
            if i == 0:
                p = 1
            else:
                p = prefix[i - 1]

            if i < len(nums) - 1:
                s = suffix[i + 1]
            else:
                s = 1

            ans.append(p * s)
    
        return ans
