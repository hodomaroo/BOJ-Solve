import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
dx,dy = [1,0,-1,0],[0,1,0,-1]
visit = [[False] * m for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[n-1][m-1] = 1

def dfs(x : int, y : int) -> int:
    if visit[x][y]: return dp[x][y]
    visit[x][y] = True

    for i in range(4):
        nx,ny = x + dx[i],y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[x][y] > board[nx][ny]:
            dp[x][y] += dfs(nx,ny)
    return dp[x][y]

print(dfs(0,0))
