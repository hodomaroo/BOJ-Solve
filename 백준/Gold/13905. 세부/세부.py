isle,brid = map(int,input().split())
s,e = map(int,input().split())
parent = [i for i in range(isle + 1)]

def find(a : int) -> int:
    stack = []
    while parent[a] != a:
        stack.append(a)
        a = parent[a]

    for child in stack:
        parent[child] = a

    return a

def isUnion(a : int , b : int):
    return find(a) == find(b)

def union(a : int ,b : int):
    if isUnion(a, b): return

    parent[find(a)] = find(b)

graph = sorted([list(map(int,input().split())) for _ in range(brid)], key= lambda x : x[-1], reverse=True)

for a,b,v in graph:
    union(a, b)
    if isUnion(s, e):
        print(v)
        exit()
print(0)

