n = int(input())
dp = [0] * (n + 2)
work = [list(map(int,input().split())) for _ in range(n)] + [[0,0]]

for i in range(n + 1):
    dp[i] = max(dp[i - 1], dp[i])
    if i + work[i][0] <= n:
        dp[i + work[i][0]] = max(dp[i] + work[i][1], dp[i + work[i][0]])
print(dp[-2])



