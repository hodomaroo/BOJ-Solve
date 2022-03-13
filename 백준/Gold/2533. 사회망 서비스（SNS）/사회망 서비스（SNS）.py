import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input().rstrip())
graph = [[] for _ in range(n+1)]
visit = [False for _ in range(n+1)]

for _ in range(n-1):
    f,t = map(int,input().rstrip().split())
    graph[f].append(t)
    graph[t].append(f)

def dfs(node : int) -> int:
    visit[node] = True
    res = [1,0]

    for nextnode in graph[node]:    #자식이 얼리어답터일때를 취해도 됨
        if visit[nextnode]: continue
        result = dfs(nextnode)
        res[0] += min(result) #본인이 얼리어답터
        res[1] += result[0] #자식들이 얼리어답터
        
    return [res[0],res[1]]
print(min(dfs(1)))