import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
population = [0] + list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
visit = [False for _ in range(n+1)]

for _ in range(n-1):
    f,t = map(int,input().split())
    graph[f].append(t)
    graph[t].append(f)

def dfs(node : int) -> int:
    visit[node] = True
    isLeaf = True
    #내가 우수일 때 / 내가 비우수일 때
    res = [population[node],0] #자식이 우수인경우 --> 반드시 비우수 / 자식이 비우수인경우 --> 우수 or 비우수 / 자식의 자식이 비우수인경우 --> 반드시 우수
    for nextnode in graph[node]:
        if visit[nextnode]: continue
        values = dfs(nextnode)
        res[1] += max(values) if len(graph[nextnode]) > 1 else values[0] #그냥 자식이 우수일 때의 total을 모두 구하면 됨
        res[0] += values[1]
    return res
print(max(dfs(1)))






