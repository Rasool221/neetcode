# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(one: Optional[TreeNode], two: Optional[TreeNode]) -> bool:
            if not one and not two:
                return True

            if not one or not two:
                return False

            if one.val != two.val:
                return False

            left_valid = compare(one.left, two.left)
            right_valid = compare(one.right, two.right)

            return left_valid and right_valid

        def dfs(root: Optional[TreeNode]) -> bool:
            if root is None:
                return False
            
            if root.val == subRoot.val and compare(root, subRoot):
                return True

            left_valid = dfs(root.left)
            right_valid = dfs(root.right)

            return left_valid or right_valid 

        return dfs(root)
