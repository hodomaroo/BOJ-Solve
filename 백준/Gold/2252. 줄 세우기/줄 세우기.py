#위상정렬
import sys
from collections import deque
input = sys.stdin.readline

N,M = list(map(int,input().split()))
link = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
ans = []

for _ in range(M):
    after,before = list(map(int,input().split()))
    link[before].append(after)
    indegree[after] += 1

queue = deque()

for idx in range(1,N+1):
    if not indegree[idx]:
        queue.append(idx)

while queue:
    number = queue.popleft()
    ans.append(number)

    for next in link[number]:
        indegree[next] -= 1
        if not indegree[next]:
            queue.append(next)
print(*reversed(ans))



