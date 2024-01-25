class Solution:
    def dfs(self, x, y, idx) -> bool:
        # Check boundaries and if the current letter matches the word
        if not (0 <= x < self.n and 0 <= y < self.m) or self.board[x][y] != self.word[idx]:
            return False
        # Check if we have found the word
        if idx == len(self.word) - 1:
            return True

        # Save the value and mark the current cell as visited
        temp, self.board[x][y] = self.board[x][y], '#'

        # Explore all possible directions
        found = self.dfs(x+1, y, idx+1) or self.dfs(x, y+1, idx+1) or self.dfs(x, y-1, idx+1) or self.dfs(x-1, y, idx+1)

        # Revert the current cell back to its original value
        self.board[x][y] = temp
        return found

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board, self.word = board, word
        self.n, self.m = len(board), len(board[0])
        
        for i in range(self.n):
            for j in range(self.m):
                if self.dfs(i, j, 0):
                    return True
        return False
