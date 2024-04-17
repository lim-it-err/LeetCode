class Solution:
    @property
    def margin(self):
        return ord("a")-ord("A")
    def makeGood(self, s: str) -> str:
        from collections import deque
        stack = deque([])
        idx = -1
        while idx<len(s)-1:
            idx+=1
            if not stack:
                stack.append(s[idx])
                continue
            prev = stack.pop()
            cur = s[idx]
            if  abs(ord(cur)-ord(prev)) == self.margin:
                continue
            stack.append(prev)
            stack.append(cur)
        return "".join(stack)
            

