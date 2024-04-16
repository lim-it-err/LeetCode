from collections import deque
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, target_depth: int) -> Optional[TreeNode]:
        q = deque([(root, 1)])
        if target_depth == 1:
            head = TreeNode(val)
            head.left = root
            return head
        while q:
            cur = q.popleft()
            node, depth = cur
            if depth == target_depth:
                return root
            if depth == target_depth-1:
                if node.left:
                    tmp = node.left
                    node.left = TreeNode(val, left=tmp)
                else:
                    node.left = TreeNode(val)
                if node.right:
                    tmp = node.right
                    node.right = TreeNode(val, right=tmp)
                else:
                    node.right = TreeNode(val)
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))
        return root