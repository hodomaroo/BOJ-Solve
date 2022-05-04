import sys
sys.setrecursionlimit(250000)
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[-1]*n for _ in range(n)]

dx,dy = [0,0,1,-1],[1,-1,0,0]
def in_range(x,y):
    return 0<=x<n and 0<=y<n

def dfs(x,y):
    global max_value
    if visited[x][y] != -1: return visited[x][y] # 적어도 한번은 방문 -->
    visited[x][y] = 0

    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y
        if in_range(nx,ny) and graph[nx][ny] > graph[x][y]: #--> 현재 위치보다 높은 위치어야 간선이 이어짐
            visited[x][y] = max(dfs(nx, ny) + 1, visited[x][y])

    return visited[x][y]

max_value = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == -1:
            max_value = max(dfs(i,j),max_value)
print(max_value+1)