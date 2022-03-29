import sys

input = sys.stdin.readline

n,m,k = map(int,input().rstrip().split())
board = [input().rstrip() for _ in range(n)]
pattern = [input().rstrip() for _ in range(k)]
patternCounter = {pat : 0 for pat in pattern}

wordByLength = [set() for _ in range(10)]
for pat in pattern:
    for i in range(len(pat)):
        wordByLength[i].add(pat[:i+1])

dx,dy = [1,0,-1,0,1,1,-1,-1],[0,1,0,-1,1,-1,1,-1]

def dfs(x : int, y : int, string : str) -> None:
    #print(x,y,string)
    if string in patternCounter:
        patternCounter[string] += 1

    for i in range(8):
        nx, ny = (x + dx[i]), (y + dy[i])
        if nx == n: nx = 0
        elif nx == -1: nx = n-1

        if ny == m: ny = 0
        elif ny == -1: ny = m-1

        nextString = string + board[nx][ny]
        if nextString not in wordByLength[len(string)]: continue
        dfs(nx,ny,nextString)

for i in range(n):
    for j in range(m):
        if board[i][j] not in wordByLength[0]: continue
        dfs(i,j,board[i][j])

for pat in pattern:
    print(patternCounter[pat])
