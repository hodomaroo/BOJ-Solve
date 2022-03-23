n = int(input())
card = [list(map(int,input().split())) for _ in range(2)]
#print(*card,sep="\n")

dp = [[-float("inf")] * (n+1) for _ in range(n+1)]
dp[0][0] = 0
maxV = 0
for j in range(n+1):  #오른쪽 사용 개수
    for i in range(n+1): #왼쪽 사용 개수
        if i and j != n:   dp[i][j] = max(dp[i - 1][j], dp[i][j])
        if i and j: dp[i][j] = max(dp[i - 1][j - 1], dp[i][j])

        if j and i != n and (card[0][i] > card[1][j - 1]):
            dp[i][j] = max(dp[i][j - 1] + card[1][j - 1], dp[i][j])

        maxV = max(maxV,dp[i][j])
print(maxV)
