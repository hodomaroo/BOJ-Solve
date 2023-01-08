n,m= map(int, input().split())
x,y = map(int,input().split())

dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][1] = 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

dp[0][1] = 0
#print(*dp, sep = "\n")
print((dp[x][y] * dp[n - x + 1][m - y + 1]) % 1000007)

