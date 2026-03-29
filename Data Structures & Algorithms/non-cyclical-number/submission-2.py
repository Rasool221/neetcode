class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(n: int) -> int:
            k = n % 10
            n = n // 10
            ans = k ** 2
    
            while k != 0:
                k = n % 10
                n = n // 10
                ans += k ** 2
    
            return ans 

        seen = set()
        result = helper(n)

        while result != 1:
            if result in seen:
                break
    
            seen.add(result)
            result = helper(result)
        
        return result != 1