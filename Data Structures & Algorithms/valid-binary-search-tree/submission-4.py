# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        interval = [-9999, 9999]

        # def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
        #     if node is None:
        #         return [-9999, 9999]

        #     cur_counts = [0, 0]
        #     if node.left:
        #         counts_left = dfs(node.left)
        #         cur_counts[0] = max(counts_left[0], node.left.val)

        #     if node.right:
        #         counts_right = dfs(node.right)
        #         cur_counts[1] = max(counts_right[1], node.right.val)

        #     return cur_counts

        # counts = dfs(root)
        # return counts[0] < root.val and counts[1] > root.val

        def is_bst_dfs(node: Optional[TreeNode]) -> bool:
            if node is None:
                return True

            if node.val is None:
                return False

            is_valid = False
            if not node.right and not node.left:
                is_valid = True
            if node.left:
                is_valid = node.val > node.left.val
            if node.right:
                is_valid = is_valid and node.val < node.right.val


            is_left_valid = is_bst_dfs(node.left)
            is_right_valid = is_bst_dfs(node.right)

            return is_left_valid and is_right_valid and is_valid

        return is_bst_dfs(root)

