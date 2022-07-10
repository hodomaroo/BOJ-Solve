d,n,m = map(int,input().split())
dist = sorted([0] + [int(input()) for i in range(n)] + [d])
l,r = 1,d + 1

while l + 1 < r:
    mid = (l + r) // 2

    point = 0
    count = 0
    for i in range(1, len(dist)):
        if dist[i] - dist[point] < mid:
            count += 1
        else:
            point = i
    if count > m:
        r = mid
    else:
        l = mid

print(l)
