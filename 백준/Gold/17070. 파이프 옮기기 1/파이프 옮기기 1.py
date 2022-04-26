n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]

dp[0][0] = [0,1,0]
dx, dy = [1, 0, 1], [0, 1, 1]
#0 : 아래 1 : 오른쪽 2 : 대각선


for i in range(n):
    for j in range(n):
        if board[i][j]: continue

        flg = False
        for d in range(3):
            if i == 0 and j == 0 and d != 1: continue
            if d == 2 and flg: continue #대각선 진행 불가
            nx, ny = i + dx[d], j + dy[d]
            if not (0 <= nx < n and 0 <= ny < n and not board[nx][ny]):
                flg = True
                continue
            dp[nx][ny][d] = dp[i][j][d] + dp[i][j][2] if d < 2 else sum(dp[i][j]) #같은 방향 / 대각선

#print(*dp,sep="\n")
print(sum(dp[-1][-1]))