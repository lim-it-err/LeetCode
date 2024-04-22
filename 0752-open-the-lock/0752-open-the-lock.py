from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = [[[[False for _ in range(10)] for _ in range(10)] for _ in range(10)] for _ in range(10)]
        combinations = [[0, 0, 0, 1], [0, 0, 0, -1], [0, 0, 1, 0], [0, 0, -1, 0], [1, 0, 0, 0], [-1, 0, 0, 0],
                        [0, 1, 0, 0], [0, -1, 0, 0]]
        
        q2 = deque([("0000")])
        if "0000" in deadends:
            return -1
        
        if target == "0000":
            return 0
        for deadend in deadends:
            a, b, c, d = map(int, deadend)
            visited[a][b][c][d] = -1
        cnt = -1
        while q2:
            q = q2.copy()
            q2 = deque()
            cnt += 1
            while q:
                cur = q.popleft()
                a, b, c, d = map(int, cur)
                for combination in combinations:
                    da, db, dc, dd = combination
                    na, nb, nc, nd = (a + da) % 10, (b + db) % 10, (c + dc) % 10, (d + dd) % 10
                    next_str = str(na) + str(nb) + str(nc) + str(nd)
                    if target == next_str:
                        print(cur)
                        if visited[na][nb][nc][nd] == -1:
                            return -1
                        return cnt + 1
                    if visited[na][nb][nc][nd] != 0:
                        continue
                    visited[na][nb][nc][nd] = 1
                    q2.append(next_str)
        return -1