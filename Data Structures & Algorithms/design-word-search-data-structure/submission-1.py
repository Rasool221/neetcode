# i think this is basically my solution for building a prefix tree, with
# the addition of the "." logic to any character (besides sentinel character)
# the tricky bit is that we have to check every possibility for "." to satisfy 
# the condition there is more than one "." in the path. For example, we cant randomly
# pick a path where only 1 more letter exists if ".." is passed and there is a possibility of 
# 2 letters we didnt pick. 
# how do we do that efficiently? 
# at most, there will be 2 dots according to the problem description
# it alsmost seems like at every level of the tree, we must store the depth of each path below it
# for example if we insert "dog":
# {
#     "@": {
#         "d": 2 # d has a depth of 2
#     },
#     "d": {
#         "@": {
#             "o":  1 # o has a depth of 1
#         },
#         "o": {
#             "@": {
#                 "g": 0 # sentinel isn't counted
#             },
#             "g": {
#                 "#": True
#             }
#         }
#     }
# }
# and then if "doge" is inserted you can guess what that would look like
# i think that works, because we can scan at each iteration how many levels each next key goes and
# pick the right one.
# we just have to make sure we update the paths at every insert, which is easy to do and calculate
# question is, enumerating the "@" map at every search level, is that worse than O(n)?
# well, at most 2 dots are given, so the most lookups we can get into "@" is if the input is ".." with any char
# ahh but what if we get "..a" as an input, i dont think our current approach handles that, we only count depth 
# rather than also some info to pick the right path to get an "a" at the end
# maybe im overcomplicating it, but what if we store depth AND full word?
# i think that's pretty complicated. can we just re-use existing methods, like recursing when we hit a "."?
# let's try that first

class WordDictionary:
    def __init__(self):
        self.trie = {}
        self.sentinel = "#"       

    def addWord(self, word: str) -> None:
        last = self.trie
        for i in range(len(word)):
            c = word[i]
            flag = i == len(word) - 1

            if c not in last:
                last[c] = {}

            if flag:
                last[c][self.sentinel] = True

            last = last[c]

    def search(self, word: str, last: dict | None = None) -> bool:
        if last is None:
            last = self.trie
        
        for i in range(len(word)):
            c = word[i]

            if c == ".":
                possible_chars = last.keys()
                found = False
                for pc in possible_chars:
                    possible_last = last[pc]
                    if pc == "#": # skipping sentinel
                        continue

                    if self.search(word[i+1:], possible_last):
                       found = True
                       break
                
                return found 
            
            if c not in last:
                return False
            
            last = last[c]

        return last[self.sentinel] == True
