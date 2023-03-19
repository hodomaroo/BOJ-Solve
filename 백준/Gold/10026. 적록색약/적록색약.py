from collections import deque


n = int(input())
board = [input() for _ in range(n)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
visit = [[False] * n for _ in range(n)]


def bfs(x: int, y: int):
    visit[x][y] = True
    q = deque([(x, y)])
    while q:
        curX, curY = q.popleft()
        for i in range(4):
            nx, ny = curX + dx[i], curY + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and board[x][y] == board[nx][ny]:
                q.append((nx, ny))
                visit[nx][ny] = True


countNormal = 0
for i in range(n):
    for j in range(n):
        if visit[i][j]:
            continue
        countNormal += 1
        bfs(i, j)


# board = list(map(lambda x : x.replace("G","R"), v for v in board))

for i in range(n):
    board[i] = board[i].replace('G', 'R')
    visit[i] = [False] * n
#print(*board, sep="\n")

countAbnormal = 0
for i in range(n):
    for j in range(n):
        if visit[i][j]:
            continue
        countAbnormal += 1
        bfs(i, j)
print(countNormal, countAbnormal)
