def traverseDP(node : int, prev : int) -> int:
    parentCost = float("inf")
    childCost = float("inf") if len(graph[node]) == 1 and node else 0

    for nextnode,cost in graph[node]:
        if nextnode == prev:
            parentCost = cost
            continue
        childCost += traverseDP(nextnode,node)
    return min(parentCost,childCost)

for _ in range(int(input())):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n)]
    answer = 0
    dp = [0] * n
    for _ in range(m):
        a,b,cost = map(int,input().split())
        graph[a-1].append((b-1,cost))
        graph[b-1].append((a-1,cost))
    print(traverseDP(0, -1))
"""
1
4 3
1 2 1000
2 3 1
2 4 1
"""