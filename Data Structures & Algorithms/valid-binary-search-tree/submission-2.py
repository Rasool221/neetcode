# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], last_val: int, left: bool) -> bool:
            if node is None:
                return True 

            if left:
                if node.val >= last_val:
                    return False
            elif node.val <= last_val:
                return False

            left_valid = dfs(node.left, node.val, True)
            right_valid = dfs(node.right, node.val, False)

            return right_valid and left_valid

        return dfs(root, root.val+1, True)