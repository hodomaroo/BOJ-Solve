n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
dp = [[float("inf")] * m for _ in range(n)]
dp[-1][-1] = 0

for i in range(n-1,-1,-1):
    for j in range(m-1,-1,-1):
        for dx in range(i):
            if abs(i - dx) > board[dx][j]: continue
            dp[dx][j] = min(dp[dx][j],dp[i][j] + 1)

        for dy in range(j):
            if abs(j - dy) > board[i][dy]: continue
            dp[i][dy] = min(dp[i][dy], dp[i][j] + 1)
print(dp[0][0])

#print(*dp,sep="\n")




