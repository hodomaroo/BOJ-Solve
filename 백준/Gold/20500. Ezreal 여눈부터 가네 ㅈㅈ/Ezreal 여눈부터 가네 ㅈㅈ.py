n = int(input())
dp = [[0] * 15 for _ in range(n)]
dp[0][1] = dp[0][5] = 1

for i in range(n-1):
    for j in range(15):
        dp[i + 1][((j * 10) + 1) % 15] += dp[i][j]
        dp[i + 1][((j * 10) + 1) % 15] %= 1000000007
        dp[i + 1][((j * 10) + 5) % 15] += dp[i][j]
        dp[i + 1][((j * 10) + 5) % 15] %= 1000000007
print(dp[n-1][0])



