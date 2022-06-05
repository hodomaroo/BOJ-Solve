n,m = map(int,input().split())
graph = [[] for _ in range(n)]
visit = [False] * n


def dfs(node : int, depth : int) -> int:
    if depth == 4: return True
    visit[node] = True

    for nextnode in graph[node]:
        if visit[nextnode]: continue
        if dfs(nextnode,depth + 1): return True

    visit[node] = False

    return False


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for v in range(n): #모든 노드에서 한번씩은
    if dfs(v,0):
        print(1)
        exit(0)
print(0)


