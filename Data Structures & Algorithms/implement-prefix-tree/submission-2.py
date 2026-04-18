# let's say we insert "dog", the tree would look like:
#      d
#    /   
#   o
#  /
# g
# then if we insert "search", what would the tree look like?
# i think we start with a tree where all nodes are the alphabet:
#  a
#   \
#    b
#     \ 
#      c
# and so forth.
# when words are inserted, we branch off the beginning of the first letter?
# or maybe we just add a new head and set the head? that doesn't make sense, since the 
# ordering of the tree represents the beginning letter. but if we create a tree with 
# the alphabet, how do we know that a prefix has been submitted, like one letter?
# we can keep a boolean flag alongside the letter in the tree node datastructure, although that works, seems a bit hacky i think
# if we do that, we can just do bfs or dfs to traverse the tree and find the letter
# ah we can subvert the root node issue with just a blank character, and we should do level order traversal (bst)
# ah but i need more than just left and right nodes, i need a tree where it can have multiple children
# and i can use a set for each level of the tree
# actually, i can implement all of this in a hashmap instead of an actual tree
# to make lookups efficient
# for example, if we insert "dog", the trie would look like:
# {
#     "": {
#         "d": {
#             "o": {
#                 "g"
#             }
#         }
#     }
# }
# then if we insert "door", it would look like:
# {
#     "": {
#         "d": {
#             "o": {
#                 "g",
#                 "o": {
#                     "r"
#                 }
#             }
#         }
#     }
# }
# well, now we can eliminate the need for the empty root entry actually
# so imagine both tries above without the root empty entry
# but now a problem exists:
# if "apple" is inserted, search cannot return True for "app", because "app" was not inserted as a word, just a substring
# but if "app" and "apple" both exist, search should return True for both. I think in that case we can store a boolean
# flag with every level in the map that should tell us at any point if we have a word
# we can do so by storing a tuple at every level of the next map and a boolean flag, ({}, False | True) to indicate this
# lets just say index 0 is the next map, index 1 is the flag whether that's a word or apart of a word
# we can also condense this down to just changing key to "<character>|<flag>" where flag is 0 or 1
# but to keep things "simple" and to not dedicate 1 char as a delimeter, i will use a tuple
# actually since tuples are immutable, tricky memory issues arised when i navigated the trie. i will 
# just need to pick a character and put it at the end of every entry as my sentinel, lets say "#".
# if that character exists at the last character of every level, i know that i have the end of a word

class PrefixTree:
    def __init__(self):
        self.trie = {} 
        self.sentinel = "#"

    def insert(self, word: str) -> None:
        # print(f"insert: {word=}, {self.trie=}")
        last = self.trie
        for i in range(len(word)):
            c = word[i]
            flag = i == len(word) - 1 # we only insert the sentinel if we're on the last letter, marking the end of a word

            if c not in last:
                if flag:
                    last[c + self.sentinel] = {}
                else:
                    last[c] = {}
            else:
                # updating entry while retaining children
                if flag:
                    ref = last[c] 
                    del last[c]
                    last[c + self.sentinel] = ref 

            if flag:
                last = last[c + self.sentinel]
            else:
                last = last[c]

        # print(f"insert, after: {self.trie=}")

    def search(self, word: str) -> bool:
        # print(f"search: {word=}, {self.trie=}")
        last = self.trie
        for i in range(len(word)):
            c = word[i]
            flag = i == len(word) - 1
            search = c if not flag else c + self.sentinel

            if search not in last:
                return False
            else:
                last = last[search]

        return True

    def startsWith(self, prefix: str) -> bool:
        # print(f"startsWith: {prefix=}, {self.trie=}")
        last = self.trie
        for i in range(len(prefix)):
            c = prefix[i]

            if c not in last:
                return False
            else:
                last = last[c]

        return True

        