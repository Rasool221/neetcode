# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current_node = root
        while current_node:
            n = current_node.val
            if n > p.val and n > q.val:
                current_node = current_node.left
            elif n < p.val and n < q.val:
                current_node = current_node.right
            elif n > p.val and n < q.val:
                return current_node
            elif n == p.val or n == q.val:
                return current_node
            else:
                raise ValueError("shouldnt happen")

        return None
