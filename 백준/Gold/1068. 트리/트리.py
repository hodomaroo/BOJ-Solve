n = int(input())
child = [[] for _ in range(n)]
parList = list(map(int,input().split()))
root = parList.index(-1)
for i,par in enumerate(parList):
    if par < 0: continue
    child[par].append(i)

removal = int(input())
def dfs(node : int) -> int: #count Leaf node
    count = 0
    for nextnode in child[node]:
        if nextnode == removal: continue
        count += dfs(nextnode)
    return 1 if not count else count

print(dfs(root) if removal != root else 0)




