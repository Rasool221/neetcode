# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            
            nonlocal is_balanced
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            if abs(right_height - left_height) > 1:
                is_balanced = False

            # take max because larger node extends graph downwards
            return max(left_height, right_height) + 1 

        dfs(root)

        return is_balanced