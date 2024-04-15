# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        answer = []
        s = deque([(root, 0)])
        while s:
            cur, value = s.pop()
            if cur.left is None and cur.right is None:
                answer.append(value*10+cur.val)
                continue
            if cur.left:
                s.append((cur.left, value*10+cur.val))
            if cur.right:
                s.append((cur.right, value*10+cur.val))
            print(s)
        return sum(answer)