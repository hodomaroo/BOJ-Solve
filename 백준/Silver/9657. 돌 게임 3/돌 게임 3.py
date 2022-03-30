n = int(input())
dp = [[-1] * 2 for _ in range(n+1)]
select = [1,3,4]

#dp[stone][turn] --> 돌이 stone개 있을 때 0 : SK / 1 : CY의 승리 가능 여부
def gameTheory(stone : int, turn : int) -> bool:
    if dp[stone][turn] != -1: return dp[stone][turn]
    if stone == 0:  #남은 돌이 없으면 상대가 승리함
        return 0

    for number in select:
        if stone - number < 0: break
        dp[stone][turn] = max(dp[stone][turn],not gameTheory(stone-number,not turn))

    return dp[stone][turn]
print(["CY","SK"][gameTheory(n,0)])

