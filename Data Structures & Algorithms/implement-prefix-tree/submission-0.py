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
class PrefixTree:
    def __init__(self):
        self.trie = ({}, False)

    def insert(self, word: str) -> None:
        last = self.trie
        for i in range(len(word)):
            c = word[i]
            flag = i == len(word) - 1 # we only insert the flag if we're on the last letter, marking the end of a word

            # works for "d"
            # but if "d" exists, would traverse down and eventually insert the new char(s) to the trie
            if c not in last:
                last[0][c] = ({}, flag) # True indicates this is a word

            last = last[0][c]

    def search(self, word: str) -> bool:
        # print(f"search: {word=}, {self.trie=}")
        last = self.trie
        for i in range(len(word)):
            c = word[i]
            if c not in last[0]:
                return False
            else:
                last = last[0][c]

        # print("returning", last[1] == True)
        return last[1] == True 

    def startsWith(self, prefix: str) -> bool:
        # print(f"startsWith: {prefix=}, {self.trie=}")
        last = self.trie
        for i in range(len(prefix)):
            c = prefix[i]
            if c not in last[0]:
                return False
            else:
                last = last[0][c]

        # print("returning", last[1] == True)
        return last[1] == False # asserting that what we found is NOT a word, just a substring search
        