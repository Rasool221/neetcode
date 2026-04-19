# my previous approach was absolute garbage, 
# i implemented a trie with a custom sentinel scheme in the key rather than
# in the children of that level, which makes the logic much simpler
# please dont look at my previous submission code (why are you even reading this?)

class PrefixTree:
    def __init__(self):
        self.trie = {} 
        self.sentinel = "#"

    def insert(self, word: str) -> None:
        last = self.trie
        for i in range(len(word)):
            c = word[i]
            flag = i == len(word) - 1

            if c not in last:
                last[c] = {}

            # marking the end of a word
            if flag:
                last[c][self.sentinel] = True 

            last = last[c]

    def search(self, word: str, enforce_sentinel = True) -> bool:
        last = self.trie
        for i in range(len(word)):
            c = word[i]

            if c not in last:
                return False

            last = last[c]

        # so we can re-use this method from startsWith
        if not enforce_sentinel:
            return True

        # only return True if end of word sentinel
        # exists in the last letter's children
        return self.sentinel in last 

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, enforce_sentinel=False)
        