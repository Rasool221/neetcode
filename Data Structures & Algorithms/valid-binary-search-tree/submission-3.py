# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        interval = [-9999, 9999]

        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            if node is None:
                return [-9999, 9999]

            cur_counts = [0, 0]

            counts_left = dfs(node.left)
            cur_counts[0] = max(counts_left[0], node.left.val)

            counts_right = dfs(node.right)
            cur_counts[1] = max(counts_right[1], node.right.val)

            # print("---")
            # print("node.val", node.val)
            # print('cur_counts', cur_counts)

            return cur_counts

        counts = dfs(root)
        return counts[0] < root.val and counts[1] > root.val