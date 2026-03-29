# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> list[int | None]:
            if node == None:
                return ["null"]

            cur = node.val

            is_leaf_node = not node.left and not node.right
            if is_leaf_node:
                return [cur]
 
            c = []

            left = dfs(node.left)
            c += left
        
            c += [cur]
        
            right = dfs(node.right)
            c += right

            return c

        p_arr = dfs(p)
        q_arr = dfs(q)

        if len(p_arr) != len(q_arr):
            return False

        return p_arr == q_arr

        
