n = int(input())
l,r = 0,n-1
liquids = sorted(list(map(int,input().split())))
zeroDist = float("inf")
ans = None
while l < r:
    dist = liquids[l] + liquids[r]

    if abs(dist) < zeroDist:
        zeroDist = min(zeroDist, abs(dist))
        ans = (liquids[l],liquids[r])

    if dist < 0:l += 1
    else:   r -= 1
print(*ans)