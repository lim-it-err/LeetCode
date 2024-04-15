# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        q = deque([(root, None)])
        answer = 0
        while q:
            cur, history = q.pop()
            if not (cur.left or cur.right):
                if history == "l":
                    answer+=cur.val
                    continue
            if cur.left:
                q.appendleft((cur.left, "l"))
            if cur.right:
                q.appendleft((cur.right, "r"))
            
        return answer