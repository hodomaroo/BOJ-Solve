from typing import List
from collections import Counter

n,s = map(int,input().split())
numList = list(map(int,input().split()))


prefix = [0] * n

count = 0

def dfsSelect(value : int ,index : int, numList : List, counter : Counter) -> None:
    if index == len(numList):
        counter[value] += 1
        return
    dfsSelect(value + numList[index],index + 1, numList, counter)
    dfsSelect(value , index + 1, numList, counter)

counterA = Counter()
counterB = Counter()
counterA[0] = counterB[0] = -1

dfsSelect(0,0,numList[:n//2],counterA)
dfsSelect(0,0,numList[n//2:],counterB)

#크기가 양수인 부분수열 --> 적어도 하나는 선택했어야함 --> 하나도 선택 안하는 경우 미리 빼주고 시작하기
ans = 0
ans += counterA[s] + counterB[s]
for v in counterA:
    ans += counterA[v] * counterB[s - v]

print(ans)
