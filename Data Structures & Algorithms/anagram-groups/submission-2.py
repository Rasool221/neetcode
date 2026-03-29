class Solution:
    def getKey(self, string: str) -> str:
        m = {}
        string = "".join(sorted(string))
        for c in string:
            if c not in m:
                m[c] = 1
            else:
                m[c] = m[c] + 1

        return "".join([f"|{ord(c) - 97},{o}|" for c, o in m.items()])

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}

        for s in strs:
            k = self.getKey(s)
            if k not in m:
                m[k] = [s]
            else:
                m[k].append(s)
        
        return [v for _, v in m.items()]

