n,k = map(int,input().split())
graph = [[] for _ in range(n+1)]
dp = [[0] * 51 for _ in range(n+1)]
nodeCount = [1] * (n + 1)
MOD = 1000000007

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node,parent):
    childUpdate = 0
    dp[node][1] = 1  #자기 자신 선택하기

    for nextnode in graph[node]:
        if nextnode == parent: continue

        dfs(nextnode,node)  #자식 노드 호출
        nodeCount[node] += nodeCount[nextnode]  #노드 값 추가

        if nodeCount[node] == nodeCount[nextnode] + 1:  #처음인 경우
            for i in range(nodeCount[nextnode] + 1):
                dp[node][i + 1] = (dp[node][i + 1] + dp[nextnode][i]) % MOD
        else:
            tmp = [0] * 51

            for i in range(nodeCount[node],0,-1):  #두개까지 보면 됨
                for j in range(1,nodeCount[nextnode]+1):
                    if i + j > nodeCount[node]: break
                    tmp[i + j] = (tmp[i + j] + (dp[node][i] * dp[nextnode][j]) % MOD) % MOD

            for i in range(nodeCount[node] + 1):
                dp[node][i] = (dp[node][i] + tmp[i]) % MOD
        #print(node,dp[node][:nodeCount[node] + 1])
dfs(1,-1)
ans = 0
for i in range(1,n+1):
    if nodeCount[i] < k: continue
    ans += dp[i][k]
print(ans)