class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(n: int) -> int:
            k = n
            ans = 0
            while n != 0:
                k = n % 10
                n = n // 10
                ans += k ** 2
                print(k, n, ans)
    
            return ans 

        seen = set()
        result = helper(n)
        
        while result != 1:
            if result in seen:
                break
    
            seen.add(result)
            result = helper(result)
        
        if result in seen:
            return False
        return result == 1