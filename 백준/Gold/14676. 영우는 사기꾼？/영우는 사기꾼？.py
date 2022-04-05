import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n + 1)
buildingCounts = [0] * (n + 1)

for i in range(m):
    f,t = map(int,input().split())
    graph[f].append(t) #y가 알고만 있으면 됨
    indegree[t] += 1

order = [list(map(int,input().split())) for _ in range(k)]

for mode,building in order:
    if (mode == 1 and indegree[building]) or (mode == 2 and not buildingCounts[building]):
        print("Lier!")
        exit()
    if mode == 1: #건물 새로 짓기
        buildingCounts[building] += 1

        if buildingCounts[building] == 1:
            for nextBuilding in graph[building]:
                indegree[nextBuilding] -= 1

    else:   #건물 철거 시
        buildingCounts[building] -= 1

        if not buildingCounts[building]:
            for nextBuilding in graph[building]:
                indegree[nextBuilding] += 1

print("King-God-Emperor")



