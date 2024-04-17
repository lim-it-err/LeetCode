# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        smallest = ""
        def dfs(node, cur_str):
            nonlocal smallest
            cur_str = "".join([chr(node.val+ord("a"))]+list(cur_str))
            if node.left is None and node.right is None:
                if smallest == "":
                    smallest = cur_str
                elif cur_str<smallest:
                    smallest = cur_str
                return
            if node.left:
                dfs(node.left, cur_str)
            if node.right:
                dfs(node.right, cur_str)
        dfs(root, "")
        return smallest
                