from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] or grid[i][j] == "0":
                    continue
                visited[i][j] = True
                answer+=1
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    for dx, dy in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
                        if not(0<=x+dx<len(grid) and 0<=y+dy<len(grid[0])):
                            continue
                        if visited[x+dx][y+dy] or grid[x+dx][y+dy] == "0":
                            continue
                        visited[x+dx][y+dy] = True
                        q.append((x+dx, y+dy))
        return answer