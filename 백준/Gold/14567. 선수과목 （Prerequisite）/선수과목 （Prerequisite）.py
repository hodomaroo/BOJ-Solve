import sys
from collections import  deque

input = sys.stdin.readline

N,M = list(map(int,input().split()))
graph = [[] for _ in range(N+1)]
timeflow = [1 for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]

for _ in range(M):
    f,t = list(map(int, input().split()))
    graph[f].append(t)
    indegree[t] += 1

queue = deque()
for i in range(1,N+1):
    if not indegree[i]:
       queue.append(i)

while queue:
    now = queue.popleft()

    for next in graph[now]:
        indegree[next] -= 1
        if not indegree[next]:
            queue.append(next)
            timeflow[next] = timeflow[now] + 1

print(*timeflow[1:])