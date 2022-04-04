import sys
from math import log2


input = sys.stdin.readline
area = int(log2(500000))  + 1

def GetPos(n,x):
    #이동횟수 n / 현재 위치 x
    for i in range(area-1,-1,-1):    #최대 50만번이므로 2^(log500000)의 범위 내에 존재함
        if n & (1 << i):
            x = SparseTable[i][x]   #X에서 2^i번 이동한 위치
    return x

M = int(input())

#최대 50만번 이동함
SparseTable = [[0] * (M + 1) for i in range(area)]
SparseTable[0] = [0] + list(map(int,input().split()))

for i in range(1,area):
    for j in range(1,M+1):
        SparseTable[i][j] = SparseTable[i-1][SparseTable[i-1][j]] #j에서 i칸 이동하는 위치 = j -> i // 2칸 한 위치에서 i // 2 칸 이동한 위치

for i in range(int(input())):
    n,x = map(int,input().split())
    print(GetPos(n,x))