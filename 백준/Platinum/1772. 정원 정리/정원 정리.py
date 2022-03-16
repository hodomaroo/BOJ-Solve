n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
count = [0] * (n + 1)

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dp =[[float("inf")] * 151 for _ in range(n+1)]

def dfs(node):
    dp[node][0] = 0 #0개의 노드를 삭제하는데는 0 cost
    count[node] = 1

    for nextnode in graph[node]:
        if count[nextnode]: continue    #부모 노드인 경우 패스

        childCount = dfs(nextnode)
        count[node] += count[nextnode]

        #지금까지의 삭제 경우의 수에 추가 연산하기
        for i in range(count[node]-1,-1,-1):
            for j in range(1,count[nextnode]+1):
                if i + j > count[node]: continue
                    #기존값과 비교해 갱신
                dp[node][i + j] = min(dp[nextnode][j] + dp[node][i],dp[node][i + j])
    dp[node][count[node]] = 1
dfs(1)

ans = float("inf")
for i in range(n+1):
    if count[i] < m: continue
    ans = min(ans,dp[i][count[i] - m] + (i != 1))  #m개 남기고 자르는데 코스트
print(ans)
