from collections import deque

n,m = map(int,input().split())
board = [input() for _ in range(n)]
dp = [[float("inf")] * m for _ in range(n)]
nearWall = [[False] * m for _ in range(n)]
visit = [[False] * m for _ in range(n)]
dx,dy = [1,0,-1,0],[0,1,0,-1]

s,e = 0,0
for x in range(n):
    for y in range(m):
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == "#":
                nearWall[x][y] = True
                break

        if board[x][y] == "S":
            s = (x,y)
        if board[x][y] == "E":
            e = (x,y)

queue = deque([s])
dp[s[0]][s[1]] = 0

while queue:
    x,y = queue.popleft()

    if visit[x][y]: continue
    visit[x][y] = True

    for i in range(4):
        nx,ny = x + dx[i],y + dy[i]
        if not(0 <= nx < n and 0 <= ny < m) or board[nx][ny] == "#": continue

        cost = 0 if (nearWall[x][y] and nearWall[nx][ny]) else 1

        if dp[nx][ny] > dp[x][y] + cost:
            dp[nx][ny] = dp[x][y] + cost

            if cost:
                queue.append((nx,ny))
            else:
                queue.appendleft((nx,ny))
print(dp[e[0]][e[1]])