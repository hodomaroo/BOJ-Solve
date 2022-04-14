import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
graph =[[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0 for i in range(n + 1)]

def dfs(node : int, parentNode : int):
    parent[node] = parentNode

    for nextNode in graph[node]:
        if nextNode != parentNode:
            dfs(nextNode,node)

dfs(1,-1)
print(*parent[2:],sep="\n")


