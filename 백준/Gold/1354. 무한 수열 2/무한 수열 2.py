n,p,q,x,y = map(int,input().split())
dp = {0 : 1}


def dfs(n : int) -> int:
    if n > 0 and n not in dp:
        dp[n] = dfs(n // p - x) + dfs(n // q - y)

    return dp[n] if n > 0 else 1

print(dfs(n))
