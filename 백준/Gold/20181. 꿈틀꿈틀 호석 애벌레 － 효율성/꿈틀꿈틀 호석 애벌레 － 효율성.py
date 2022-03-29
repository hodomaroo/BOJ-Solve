n,k= map(int,input().split())
food = list(map(int,input().split()))
left,right = 0,0
total = 0
dp = [0] * (len(food) + 1)


while left < len(food):
#    print(left,right,total)
    while total < k and right < len(food):
        dp[right] = max(dp[right - 1], dp[right])
        total += food[right]
        right += 1

    dp[right] = max(dp[right-1], dp[right],dp[left] + total - k)
    total -= food[left]
    left += 1

print(dp[-1])