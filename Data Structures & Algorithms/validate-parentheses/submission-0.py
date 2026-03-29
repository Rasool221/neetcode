class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        open_c = {"(", "{", "["}
        close_c = {")", "}", "]"}

        mapping = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for c in s:
            if c in open_c:
                stack.append(c)
            else:
                latest = stack.pop()
                if c not in mapping:
                    return False
                
                if mapping[c] != latest:
                    return False

        return True