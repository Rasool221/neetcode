# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        gmax = root.val

        def dfs(root: Optional[TreeNode]):
            if root is None:
                return 0

            nonlocal gmax 

            left_max = dfs(root.left)
            right_max = dfs(root.right)

            # case 1: current val is max
            gmax = max(gmax, root.val)

            # case 2: current val + left subtree
            gmax = max(gmax, root.val + left_max)

            # case 3: current val + right subtree
            gmax = max(gmax, root.val + right_max)

            # case 4: current val + left subtree + right subtree
            gmax = max(gmax, root.val + left_max + right_max)

            return root.val + max(0, left_max, right_max)

        dfs(root) # disregard because root is accounted for in case 4

        return gmax