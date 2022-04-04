import sys

input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
board = [list(input().rstrip()) for _ in range(n)]
storePos = []
count = 1

sx,sy = 0,0
for i in range(n):
    for j in range(m):
        if board[i][j] == "K":
            storePos.append((i,j))
            board[i][j] = count
            count += 1
        if board[i][j] == "S":
            sx, sy = i, j
            board[i][j] = 0

graph = [set() for _ in range(count)]

dx,dy = [1,0,-1,0],[0,1,0,-1]

def bfs(sx : int,sy : int, index : int) -> None:
    dp = [[-1] * m for _ in range(n)]

    dp[sx][sy] = 0
    q = deque([(sx,sy)])

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != "X" and dp[nx][ny] == -1:
                dp[nx][ny] = dp[x][y] + 1

                if type(board[nx][ny]) == int:
                    graph[index].add((board[nx][ny],dp[nx][ny]))
                    graph[board[nx][ny]].add((index, dp[nx][ny]))

                q.append((nx,ny))

for index,pos in enumerate(storePos):
    bfs(pos[0], pos[1], index + 1)

if len(graph[0]) < 5:
    print(-1)
    exit()

visit = [0] * 21
minCount = float("inf")

def dfs(node : int, depth : int, movement : int) -> None:
    global minCount
    if minCount <= movement: return

    if depth == 5:
        minCount = movement
        return

    visit[node] = True
    for nextnode,cost in graph[node]:
        if visit[nextnode]: continue
        dfs(nextnode,depth+1,movement+cost)
    visit[node] = False

dfs(0,0,0)
print(minCount)



