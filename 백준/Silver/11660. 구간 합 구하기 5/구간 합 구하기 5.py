import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
prefix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        prefix[i][j] = board[i][j]
        if i: prefix[i][j] += prefix[i-1][j]
        if j: prefix[i][j] += prefix[i][j-1]
        if i and j: prefix[i][j] -= prefix[i-1][j-1]
#print(*prefix,sep="\n")

for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    x1,y1,x2,y2 = x1-1,y1-1,x2-1,y2-1

    value = prefix[x2][y2]
    if x1 > 0: value -= prefix[x1-1][y2]
    if y1 > 0: value -= prefix[x2][y1-1]
    if x1 > 0 and y1 > 0: value += prefix[x1-1][y1-1]
    print(value)