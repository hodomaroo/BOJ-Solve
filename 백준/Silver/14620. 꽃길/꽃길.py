n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
check = [[False] * n for _ in range(n)]

minCost = float("inf")
qwer = [(0,1),(0,-1),(1,0),(-1,0),(0,0)]

for i in range(n+1,n * (n-1) - 1):

    if i % n in (n-1,0): continue
    #print(i)
    for j in range(i + 1, n * (n - 1) - 1):
        if j % n in (n - 1, 0): continue
        if abs(i % n - j % n) ** 2 + abs(i // n - j // n) ** 2 <= 4: continue
        for k in range(j + 1, n * (n - 1) - 1):
            if k % n in (n - 1, 0): continue
            if abs(i % n - k % n) ** 2 + abs(i // n - k // n) ** 2 <= 4: continue
            if abs(j % n - k % n) ** 2 + abs(j // n - k // n) ** 2 <= 4: continue

            total = 0

            for pos in [i,j,k]:
                for nx,ny in qwer:
                    total += board[pos // n + nx][pos % n + ny]
            #print(i, j, k, total)
            minCost = min(total,minCost)
print(minCost)



