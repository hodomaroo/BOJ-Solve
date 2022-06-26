def dfs(node : int):
    visit[node] = True

    for nextnode in graph[node]:
        if visit[nextnode]: continue
        dfs(nextnode)

for _ in range(int(input())):
    n = int(input())
    area = [list(map(int, input().split())) for _ in range(n)]
    graph = [[] for _ in range(n)]
    visit = [False] * n

    for i in range(n):
        for j in range(i):
            x,y,power = area[i]
            x2,y2,power2 = area[j]

            if pow(x2 - x, 2) + pow(y2 - y, 2) <= pow(power + power2, 2):
                graph[i].append(j)
                graph[j].append(i)
    count = 0
    for i in range(n):
        if not visit[i]:
            count += 1
            dfs(i)
    print(count)

