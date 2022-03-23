n = int(input())
#초기값은 A
dp = [[0] * 2 for _ in range(n + 1)]
dp[0][0] = 1

for i in range(1,n+1):
    dp[i][0] = dp[i-1][1]
    dp[i][1] = sum(dp[i - 1])
print(*dp[i])