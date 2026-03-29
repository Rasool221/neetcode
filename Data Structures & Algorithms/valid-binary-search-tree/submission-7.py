# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, _min: int, _max: int) -> bool:
            if node is None:
                return True

            if node.val <= _min or node.val >= _max:
                return False

            is_left_valid = dfs(node.left, _min, node.val)
            is_right_valid = dfs(node.right, node.val, _max)

            return is_left_valid and is_right_valid

        return dfs(root, float('-inf'), float('inf'))
        
        
        