from collections import deque
n,m = map(int,input().split())
board = [[0] * n for _ in range(n)]
dp = [[-1] * n for _ in range(n)]
count = 1
x,y = map(int,input().split())
dx,dy = [2,2,-2,-2,1,1,-1,-1],[1,-1,1,-1,2,-2,2,-2]

for i in range(m):
    a,b = map(int,input().split())
    board[a-1][b-1] = count
    count += 1

ansList = [0] * (count - 1)
dp[x-1][y-1] = 0

q = deque([(x-1,y-1)])

while q:
    x,y = q.popleft()
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and dp[nx][ny] == -1:
            dp[nx][ny] = dp[x][y] + 1
            if board[nx][ny]:
                ansList[board[nx][ny]-1] = dp[nx][ny]
            q.append((nx,ny))

print(*ansList)
"""
-1 -1 -1 -1 -1
-1  2 -1  0 -1
-1 -1 -1 -1 -1
 3 -1  1 -1  1
-1 -1 -1 -1 -1
"""
