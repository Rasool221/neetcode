# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        bounds = [-9999, 9999]

        # node_type: 0 -> root, 1 -> left, 2 -> right
        def dfs(node: Optional[TreeNode], node_type: int):
            if node is None:
                return 

            if node_type != 0:
                if node_type == 1:
                    bounds = [max(node.val, bounds[0]), bounds[1]]
                else:
                    bounds = [bounds[0], max(node.val, bounds[0])]

            dfs(node.left)
            dfs(node.right)

        root_val = root.val
        dfs(root)
        print("bounds", bounds)
        return root_val > bounds[0] and root_val < bounds[1]

        # node_type: 0 -> root, 1 -> left, 2 -> right
        # def dfs(node: Optional[TreeNode], bounds, node_type: int) -> bool:
        #     if node is None:
        #         return True
            
        #     condition = False
        #     if node_type == 0:
        #         condition = node.vral > bounds[0] and node.val < bounds[1]
        #     elif node_type == 1:
        #         condition = node.val < bounds[0] and node.val < bounds[1]
        #     else:
        #         condition = node.val > bounds[0] and node.val > bounds[1]

        #     bounds_for_children = [max(node.val, bounds[0]), min(node.val, bounds[1])]
        #     is_left_valid = dfs(node.left, bounds_for_children, 1)
        #     is_right_valid = dfs(node.right, bounds_for_children, 2)

        #     return condition and is_left_valid and is_right_valid

        # return dfs(root, bounds, 0)

