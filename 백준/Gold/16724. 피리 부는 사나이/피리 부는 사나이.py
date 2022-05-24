#Disjoint Set
n,m = map(int,input().split())
graph = [input() for _ in range(n)]

parent = [i for i in range(n * m)]

def find(x : int) -> int:
    stack = []
    while parent[x] != x:
        stack.append(x)
        x = parent[x]

    while stack:
        parent[stack.pop()] = x

    return x

def isUnion(x : int ,y : int) -> bool:
    return find(x) == find(y)

def union(getter : int, putter : int):
    if isUnion(getter,putter): return
    parent[find(putter)] = find(getter)

direction = {"L" : 0, "D" : 1, "R" : 2, "U" : 3}
dx,dy = [0,1,0,-1], [-1,0,1,0]

for i in range(n):
    for j in range(m):
        dir = direction[graph[i][j]]
        nx,ny = i + dx[dir], j + dy[dir]

        union(nx * m + ny, i * m + j)

parentSet = set()
for i in range(n * m):
    parentSet.add(find(i))
print(len(parentSet))







