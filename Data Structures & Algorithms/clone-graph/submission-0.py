"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# i think just a recursive creation here?
# ah recursive creation here runs into infinite loop problem
# e.g. node 2 -> node 1 -> node 2 -> node 1 ....
# so we can keep a cache/memo i think bc values should be unique
# so this is a DFS approach. a BFS approach would work as well and probably be a bit cleaner?

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # node is the object we want to deep copy
        # memo is a map of val -> object reference, so we don't recopy the same
        # one's we've done before
        def clone(node: Optional['Node'], memo: {}) -> Optional['Node']:
            if node is None:
                return None

            # preventing infinite loops
            if node.val in memo:
                return memo[node.val]

            new_node = Node(node.val)
            memo[node.val] = new_node # adding ref to cache

            if node.neighbors:
                new_node.neighbors = []
    
                for n in node.neighbors:
                    new_n = clone(n, memo)
                    if new_n:
                        new_node.neighbors.append(new_n)
    
            return new_node

        new_head = clone(node, {})
        return new_head
        