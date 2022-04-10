n = int(input())
total = 0

grid = []
for i in range(n):
    x,y = map(int,input().split())
    grid.append((x + 100000,y + 100000)) #좌표 전체 양수화

for i in range(n):
    #01 12 23 30
    x,y = grid[i]
    nx,ny = grid[(i+1)%n]

    total += (y - ny) * (x + nx) / 2
print(abs(total))


