from itertools import combinations
from collections import deque
import sys

n , m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
virus = []
dxs,dys = [1,-1,0,0],[0,0,1,-1]
wall = 0

def bfs(vlist): #m개의 바이러스 리스트 입력
    global ans
    visited = [[False]*n for _ in range(n)]
    que = deque()
    max_value = 0
    for i in vlist:
        a,b= i
        que.append(i)
        visited[a][b] = 1

    visitCount = 0
    maxTime = 1

    while que:
        dx,dy = que.popleft()
        for i in range(4):
            nx,ny=dxs[i]+dx,dys[i]+dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] != 1:
                que.append((nx,ny))###
                visitCount += 1
                visited[nx][ny] = visited[dx][dy] + 1
                if graph[nx][ny] != 2:
                    maxTime = max(visited[nx][ny], maxTime)

    return maxTime-1 if visitCount == needTovisit else float("inf")

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append((i,j))
        elif graph[i][j] == 1:
            wall += 1

needTovisit = n * n - wall - m
ans = float("inf")

for v in combinations(virus,m): #m가지의 바이러스를 뽑은 경우의수
    ans = min(bfs(v),ans)

print(ans if ans != float("inf") else -1)

