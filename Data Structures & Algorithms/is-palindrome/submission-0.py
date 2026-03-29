class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        s = s.lower()
        while l < r:
            lc = s[l]
            rc = s[r]

            print("-before")
            print("l, lc", l, lc)
            print("r, rc", r, rc)

            while not lc.isalnum():
                l += 1
                lc = s[l]

            while not rc.isalnum():
                r -= 1
                rc = s[r]

            if lc != rc:
                return False

            l += 1
            r -= 1

        return True

