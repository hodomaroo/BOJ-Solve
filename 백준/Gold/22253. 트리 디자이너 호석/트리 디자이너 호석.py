import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
graph = [[] for _ in range(n)]
dp = [[0] * 10 for _ in range(n)]
#dp[n][0~9] --> n번 노드가 off일 때 0~9까지의 가짓수 0b"0"****...(x-1)개의 가짓수

valueOfNode = list(map(int,input().split()))
MOD = 1000000007
total = 0

for _ in range(n-1):
    f,t = map(int,input().split())
    graph[f - 1].append(t - 1)
    graph[t - 1].append(f - 1)

def dfs(node : int, prev : int) -> int:
    global total
    nodeValue = 1

    for childNode in graph[node]:
        if childNode == prev: continue
        childNodeValue = dfs(childNode,node) #선택했을 때의 경우의 수

        if valueOfNode[childNode] >= valueOfNode[node]: #얘가 이전 노드보다 작거나 같으면 이전 노드를 선택한 경우도 가질 수 있음
            nodeValue = (nodeValue + childNodeValue) % MOD
        
        dp[node][valueOfNode[childNode]] += childNodeValue #이번 노드를 선택하지 않은 경우 자식 노드가 선택된 경우 / 선택되지 않은 경우에 대한 경우를 취함 (가장 높은 비트가 다르다 )

        for digit in range(10):
            dp[node][digit] = (dp[node][digit] + dp[childNode][digit]) % MOD #자식 노드가 선택되지 않은 경우을 취핢

            if digit >= valueOfNode[node]:  #취할 수 있는 경우
                nodeValue = (nodeValue + dp[childNode][digit]) % MOD

    #nodevalue는 결과적으로 이번 수를 선택했을 때 얻을 수 있는 경우의 수가 됨 --> 뒤쪽 최상위들은 전부 0이니 중복 X
    total = (nodeValue + total) % MOD
    return nodeValue #선택했을 때의 경우의 수

dfs(0,-1)
print(total)