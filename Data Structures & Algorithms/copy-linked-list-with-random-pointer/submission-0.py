"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# 2 cases 
# 1. pointing to random backwards
# 2. pointing forwards

# if pointing backwards, we can expect the random ptr to be in the map
# if its pointing forwards, we add to the map the value we need -> cur copy node
#   at every iteration, we check if cur.val = value we need, if we do, we go to val and update its random to cur node
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        m = {} # node.val -> Node

        cur = head
        prev_copy = None
        head_copy = None
        while cur:
            copy = Node(cur.val, cur.next, cur.random)

            if prev_copy is None:
                head_copy = copy
                prev_copy = copy
            else:
                prev_copy.next = copy

            prev_copy = copy
            if cur:
                m[cur] = copy

            cur = cur.next

        cur = head_copy
        while cur:
            if cur.random:
                copy_random = m[cur.random]
                cur.random = copy_random

            cur = cur.next

        return head_copy