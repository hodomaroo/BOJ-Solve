n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
dp = [[[board[i][j]] * 3 for j in range(m)] for i in range(n)]
dir = [-1, 0, 1]

for i in range(1, n):
    for j in range(m):
        for k in range(3):
            if j + dir[k] in (-1, m): 
                dp[i][j][k] = float("inf")
                continue
            dp[i][j][k] += min(dp[i - 1][j + dir[k]][v] for v in range(3) if k != v)
            #해당 방향에 있는 값은... 

#print(*dp, sep = "\n")
print(min(min(v) for v in dp[-1]))
            

