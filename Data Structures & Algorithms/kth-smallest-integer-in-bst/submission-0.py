# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 1
        v = 0 

        def dfs(root: Optional[TreeNode]): 
            nonlocal n
            nonlocal v

            print(f"{root.val=} {n=} {v=}")

            # first check left
            if root.left:
                dfs(root.left)

            # then check self
            if n == k:
                v = root.val

            n += 1 # we visited the node, so we increment
            
            # finally check right
            if root.right:
                dfs(root.right)

        dfs(root)
        return v