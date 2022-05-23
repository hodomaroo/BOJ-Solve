#Union-Find Or BFS

#귀찮으니 Union-Find 풀이

n = int(input())

parent = [i for i in range(n + 1)]
graph = [[] for i in range(n + 1)]

def find(a : int) -> int:
    updateStack = []
    while parent[a] != a:
        updateStack.append(a)
        a = parent[a]

    for node in updateStack:
        parent[node] = a

    return a

def isUnion(a : int, b : int) -> bool:
    return find(a) == find(b)

def union(a : int, b : int):
    if isUnion(a,b): return
    parent[find(a)] = parent[find(b)] #union

for i in range(n - 2):
    union(*list(map(int,input().split())))

for i in range(1, n + 1):
    if find(i) != find(1):
        print(1,i)
        exit()
