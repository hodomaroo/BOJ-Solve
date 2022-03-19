#효율적인 해킹
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]

try:
    while True:
        f, t = map(int, input().split())
        graph[t - 1].append(f - 1)  # t -> f로 전파 가능
        graph[f - 1].append(t - 1)  # t -> f로 전파 가능
except: pass

def bfs(node : int) -> int:
    queue = deque([(node)])
    dp = [None] * n
    dp[node] = 0
    maxCost = 0

    while queue:
        node = queue.popleft()
        for nextnode in graph[node]:
            if dp[nextnode] != None: continue
            maxCost = dp[nextnode] = dp[node] + 1
            queue.append(nextnode)
    #print(dp)
    return maxCost

maxStack = []
maxScore = float("inf")
for i in range(n):
    score = bfs(i)
    if score < maxScore:
        maxScore = score
        maxStack = [i+1]

    elif score == maxScore:
        maxStack.append(i+1)

print(maxScore,len(maxStack))
print(*sorted(maxStack))
