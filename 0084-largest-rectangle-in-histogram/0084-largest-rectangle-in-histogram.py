class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_value = -1
    
    def put(self, idx, cur_value):
        while self.stack:
            popped = self.stack.pop()
            if popped[0]< cur_value:
                self.stack.append(popped)
                break
            if self.stack:
                peeked = self.stack[-1]
            else:
                peeked = (0, -1)
            self.max_value = max(self.max_value, (idx-peeked[1]-1)*popped[0])
        if not self.stack:
            self.stack.append((cur_value, idx))
            return

        popped = self.stack.pop()
        if popped[0]>=cur_value:
            self.stack.append(popped)
            return
        self.stack.append(popped)
        self.stack.append((cur_value, idx))

    def complete(self, total_length):
        while self.stack:
            popped = self.stack.pop()
            if not self.stack:
                peeked = (0, -1)
            else:
                peeked = self.stack[-1]
            self.max_value = max(self.max_value, (total_length-peeked[1]-1)*popped[0])
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = MaxStack()
        for i, height in enumerate(heights):
            stack.put(i, height)
        stack.complete(len(heights))
        return stack.max_value