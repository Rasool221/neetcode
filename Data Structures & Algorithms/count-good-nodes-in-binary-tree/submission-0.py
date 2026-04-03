# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 1 # root is always provided, its always a good node

        def dfs(root: Optional[TreeNode], nmax: int):
            if not root:
                return

            nonlocal good_nodes

            if root.val >= nmax:
                good_nodes += 1

            new_nmax = max(nmax, root.val)
            dfs(root.left, new_nmax)
            dfs(root.right, new_nmax)

        if root.left:
            dfs(root.left, root.val)
        if root.right:
            dfs(root.right, root.val)

        return good_nodes