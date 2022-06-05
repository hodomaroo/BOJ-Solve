from collections import deque

dx,dy = [0,-1,0,1],[-1,0,1,0]

def bfs(start : int, groupCode : int):
    curSize = 0
    queue = deque([start])
    group[start[0]][start[1]] = groupCode

    while queue:
        x,y = queue.popleft()
        curSize += 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not (board[x][y] >> i & 1)  and not group[nx][ny]:

                group[nx][ny] = groupCode
                queue.append((nx, ny))
    groupSize.append(curSize)


m,n = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
group = [[0] * m for _ in range(n)]
groupSize = [0]

biggestUnionedRoom = 0
for i in range(n):
    for j in range(m):
        if group[i][j]: continue
        bfs((i, j), len(groupSize))

for x in range(n):
    for y in range(m):
        for d in [1,2]:
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and group[nx][ny] != group[x][y]:
                biggestUnionedRoom = max(biggestUnionedRoom, groupSize[group[x][y]] + groupSize[group[nx][ny]])

print(len(groupSize) - 1 ,max(groupSize),biggestUnionedRoom, sep="\n")
