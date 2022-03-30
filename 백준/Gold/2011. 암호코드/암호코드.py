import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline
#그냥 인덱스..
n = list(map(int,list(input().rstrip())))
dp = [-1] * (len(n) + 2)   #x번째 인덱스에서 시작할 때 경우의 수
dp[-2] = 1
dp[-1] = 0
if len(n) <= 1:
    print(int(n[0] > 0))
    exit()
n.extend([0,0])

#print(dp)
def dfs(index : int) -> int:
    if dp[index] != -1: return dp[index]

    dp[index] = 0
    #print(index)
    if n[index] > 0:
        dp[index] = (dfs(index+1) + (0 if not (n[index] * 10 + n[index+1] <= 26) else dfs(index+2))) % 1000000
    return dp[index]
print(dfs(0))
#print(dp)