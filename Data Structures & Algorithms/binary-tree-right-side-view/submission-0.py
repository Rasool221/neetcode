# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

# level order traversal, keep set of level added
# when traversing, favor right sides first, check if level in set, if it isnt, add it to answers arr
# return answers arr

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        a = []
        m = set()

        if root:
            q.append((root, 1))

        while len(q) > 0:
            entry = q.popleft()
            node = entry[0]
            level = entry[1]

            if node is None:
                continue

            if level not in m:
                a.append(node.val)
                m.add(level)

            # favoring right hand side first
            if node.right:
                q.append((node.right, level + 1))
    
            if node.left:
                q.append((node.left, level + 1))


        return a