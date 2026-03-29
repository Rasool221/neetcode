class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        s = s.lower()
        while l < r:
            lc = s[l]
            rc = s[r]

            while not lc.isalnum() and l < r:
                l += 1
                lc = s[l]

            while not rc.isalnum() and l < r:
                r -= 1
                rc = s[r]

            if lc != rc:
                return False

            l += 1
            r -= 1

        return True

