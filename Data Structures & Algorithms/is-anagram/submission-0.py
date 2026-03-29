class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return s[::-1] == t