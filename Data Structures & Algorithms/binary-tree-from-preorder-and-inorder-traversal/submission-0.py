# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        lookup = {val: i for i, val in enumerate(inorder)}

        def recurse(pre_start, pre_end, ino_start, ino_end):
            if pre_start >= pre_end or ino_start >= ino_end:
                return None

            p = preorder[pre_start]
            root = TreeNode(p)

            pos_in_inorder = lookup[p]
            size_left = pos_in_inorder - ino_start

            root.left = recurse(pre_start + 1, pre_start + 1 + size_left, ino_start, pos_in_inorder)
            root.right = recurse(pre_start + 1 + size_left, pre_end, pos_in_inorder + 1, ino_end)

            return root

        return recurse(0, len(preorder), 0, len(inorder))