from heapq import heappop,heappush

inf = float("inf")
n,m = map(int, input().split())

costTable = [[[inf, inf] for _ in range(m)] for _ in range(n)]
visit = [[False] * m for _ in range(n)]
board = [input() for _ in range(n)]
s,f = 0,0

for i in range(n):
    for j in range(m):
        if board[i][j] == "S":
            s = (i,j)
        elif board[i][j] == "F":
            f = (i,j)


dx,dy = [1,0,-1,0],[0,1,0,-1]

def nearCheck(x : int, y : int) -> int:
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == "g":    return 1

    return 0
sx,sy = s

costTable[sx][sy] = [0,0]
heap = [(0,0,sx,sy)]

while heap:
    trash, nearTrash, x, y = heappop(heap)
    if visit[x][y]: continue
    visit[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            nexTrash = trash + (board[nx][ny] == "g")
            nextNearTrash = nearTrash + (nearCheck(nx, ny) if board[nx][ny] != "g" else 0)
            if [nexTrash,nextNearTrash] < costTable[nx][ny]:
                costTable[nx][ny] = [nexTrash,nextNearTrash]
                heappush(heap, (nexTrash, nextNearTrash, nx, ny))
#print(*costTable,sep="\n")
ansTrash,ansNearTrash = costTable[f[0]][f[1]]
print(ansTrash,ansNearTrash - nearCheck(f[0],f[1]))