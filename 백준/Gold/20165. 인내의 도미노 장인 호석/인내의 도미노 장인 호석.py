n,m,r = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
isStanding = [[True] * m for _ in range(n)]
commands = [list(input().rstrip().split()) for _ in range(r * 2)]
score = 0

dirDict = {"E" : 1, "N" : 2,"S" : 0,"W" : 3}

dx,dy = [1,0,-1,0],[0,1,0,-1]

for i in range(r):  #라운드만큼 진행
    command = commands[i * 2]

    x,y = int(command[0]) - 1,int(command[1]) - 1
    point = 1
    while 0 <= x < n and 0 <= y < m and point:
        if isStanding[x][y]:
            isStanding[x][y] = False
            score += 1
            point = max(point - 1,board[x][y] - 1)
        else: point -= 1

        x, y = x + dx[dirDict[command[2]]], y + dy[dirDict[command[2]]]
    #print(*isStanding, sep="\n", end="\n\n")
    isStanding[int(commands[i*2+1][0]) - 1][int(commands[i*2+1][1]) - 1] = True

    #print(*isStanding,sep="\n",end="\n\n")
print(score)
for line in isStanding:
    print(*list(["F","S"][boolean] for boolean in line))
