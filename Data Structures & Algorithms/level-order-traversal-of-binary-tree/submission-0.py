# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        l = 1

        a = [[]]
        q = deque()

        if root is None:
            return []

        q.append((root, l))

        while len(q) > 0:
            c = q.popleft()
            v = c[0]
            n = c[1]

            if n - 1 == len(a):
                a.append([v.val])
            else:
                a[-1].append(v.val)

            if v.left:
                q.append((v.left, n+1))

            if v.right:
                q.append((v.right, n+1))

        return a
