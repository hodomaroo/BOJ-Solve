n,m = map(int,input().split())
board = [list(map(int,list(input()))) for _ in range(n)]
dp = [[0] * (m+1) for _ in range(n+1)]
maxArea = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1]) * board[i-1][j-1] + board[i-1][j-1]
        maxArea = max(maxArea,dp[i][j])
print(maxArea ** 2)