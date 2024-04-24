class Solution:
    def calc(self, n):
        self.dp[n] = self.dp[n-1]+self.dp[n-2]+self.dp[n-3]
        return n+self.dp[n-1]+self.dp[n-2]
    def tribonacci(self, n: int) -> int:
        self.dp = [0 for _ in range(max(3, n+1))]
        self.dp[0], self.dp[1], self.dp[2] = 0, 1, 1
        if n>=3:
            for i in range(3, n+1):
                self.calc(i)
        return self.dp[n]