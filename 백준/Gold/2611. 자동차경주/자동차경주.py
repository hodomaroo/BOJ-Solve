import sys
from typing import List
from collections import deque
input = sys.stdin.readline

#dfs 풀이는 간단할거같고..
#bfs 위상정렬 풀이로 풀어보면...

#일단 1에서 시작 -->  indegree가 0인 애들은 갱신 종료 -->
#쭉 진행하면서 final DP값만 취하기
ansRoute = [1]

def backTracking(node : int) -> List: # 거슬러 올라가기
    #하나만 취하면 되므로 그냥 쭉쭉 따라가면 됨
    global ansRoute

    for nextnode,cost in rv_graph[node]:

        if nextnode == 1 and dp[node] - cost == 0:
            print(*(ansRoute + [1])[::-1])
            exit()

        if dp[nextnode] == dp[node] - cost:
            ansRoute.append(nextnode)
            backTracking(nextnode)


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
rv_graph = [[] for _ in range(n + 1)]

indegree = [0] * (n + 1)
dp = [-float("inf")] * (n + 1)

for i in range(m):
    f,t,cost = map(int,input().split())
    graph[f].append((t, cost))
    rv_graph[t].append((f, cost))
    indegree[t] += 1

queue = deque([1])  #1번 노드에서 무조건 시작

#모든 노드는 1번 의존성을 가짐 --> 적어도 하나의 노드는 부모로 1만을 가져야 한다 --> 위상정렬 가능
dp[1] = 0
while indegree[1]:
    node = queue.popleft()

    for nextnode,cost in graph[node]:
        indegree[nextnode] -= 1
        dp[nextnode] = max(dp[nextnode], dp[node] + cost)

        if not indegree[nextnode]:
            queue.append(nextnode)

print(dp[1])
backTracking(1)




