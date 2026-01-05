# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        global_path = []
        path = []

        def dfs(node, path):
            if node is None:
                return

            # append current node
            path.append(str(node.val))

            if node.left is None and node.right is None:
                global_path.append("->".join(path))
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            
            # backtracking 
            path.pop()

        dfs(root, path)    
        return global_path