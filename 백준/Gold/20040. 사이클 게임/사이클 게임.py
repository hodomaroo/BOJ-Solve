import sys

input = sys.stdin.readline

n,m = map(int,input().split())
parent = [i for i in range(n + 1)]
rank = [0 for i in range(n + 1)]

def find(a : int) -> int:
    if parent[a] == a:  return a

    parent[a] = find(parent[a])
    return parent[a]

def isunion(a,b) -> bool:
    return find(a) == find(b)
def union(a,b) -> bool:
    if isunion(a,b): return

    if rank[find(a)] > rank[find(b)]:   a, b = b, a
    rank[find(b)] += rank[find(a)] == rank[find(b)]
    parent[find(a)] = find(b)


for i in range(1,m + 1):
    a,b = map(int,input().split())
    if isunion(a,b):
        print(i)
        exit()
    union(a,b)

print(0)

