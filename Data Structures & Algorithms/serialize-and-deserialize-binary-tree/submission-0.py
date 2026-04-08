# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        def dfs(node: Optional[TreeNode]) -> str:
            if node is None:
                return "#"

            left = dfs(node.left)
            right = dfs(node.right)

            return str(node.val) + "," + str(left) + "," + str(right) 

        return dfs(root)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None

        arr = data.split(",")
        q = deque(arr)

        def dfs() -> TreeNode:
            item = q.popleft()

            if item == "#":
                return None
            
            node = TreeNode(item)
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs() 
