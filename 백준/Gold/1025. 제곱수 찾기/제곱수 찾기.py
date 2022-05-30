import sys
from math import sqrt
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
board = [list(map(int,list(input().rstrip()))) for _ in range(n)]
perfectPowSet = set(v*v for v in range(int(sqrt(pow(10,max(n,m)))) + 1))

ans = -1
for i in range(n * m):
    x, y = i // m, i % m
    for dx in range(-x, n - x, 1):  # 최대 이만큼 전개 가능
        for dy in range(-y, m - y,1):

            px, py = x, y
            v = 0
            while 0 <= px < n and 0 <= py < m:
                v = v * 10 + board[px][py]
                px, py = px + dx, py + dy
                if v in perfectPowSet:
                    ans = max(ans, v)
                if not dx and not dy: break
print(ans)
