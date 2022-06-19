n,p,q = map(int,input().split())
dp = {0 : 1}


def dfs(n : int) -> int:
    if n not in dp:
        dp[n] = dfs(n // p) + dfs(n // q)

    return dp[n]

print(dfs(n))
