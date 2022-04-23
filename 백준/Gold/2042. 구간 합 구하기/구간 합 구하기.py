import sys
input = sys.stdin.readline

from math import log2,ceil

n,m,k = map(int,input().split())
depth = ceil(log2(n)) + 1
#데이터 - 순으로 해서 넣어주기 --?

segmentTreeNodes = [0] * (pow(2,depth))
segBaseNodes = pow(2,depth-1)

#print(len(segmentTreeNodes),segBaseNodes)
def getNthNodes(index : int) -> int:
    return len(segmentTreeNodes) - segBaseNodes + index

def updateValue(targetNode : int, value : int): #갱신하면서 올라가기
    targetNode = getNthNodes(targetNode)
    #print(targetNode,value)

    diff = segmentTreeNodes[targetNode] - value #
    while targetNode:
        segmentTreeNodes[targetNode] -= diff
        targetNode //= 2 #위로 올라가면서 부모값 갱신

def getSegmentSum(wantLeft : int, wantRight : int) -> int:
    return getAreaSum(1,0,segBaseNodes-1,wantLeft,wantRight)

def getAreaSum(node : int, start: int, end: int, wantLeft: int, wantRight: int) -> int:
    #원하는 영역의 합 구하기
    #print(node,start,end,wantLeft,wantRight)
    mid = (start + end) // 2
    if (start,end) == (wantLeft,wantRight): #영역이 동일하면 해당 세그먼트 값 리턴하기
        return segmentTreeNodes[node]

    areaSum = 0
    if wantLeft <= mid:
        areaSum += getAreaSum(node * 2, start, mid, wantLeft, min(wantRight, mid))

    if wantRight > mid:
        areaSum += getAreaSum(node * 2 + 1, mid + 1, end, max(mid+1,wantLeft), wantRight)

    return areaSum

def displaySegmentTree():
    index = 1
    dis = 1
    while index < len(segmentTreeNodes):
        sepa = segBaseNodes // dis - 1
        print(" " * sepa,end = "")
        print(*segmentTreeNodes[index: index + dis],sep=" " * (sepa * 2 + 1))
        index += dis
        dis *= 2

#displaySegmentTree()
numberList = [int(input()) for _ in range(n)]
for i in range(len(numberList)):
    updateValue(i,numberList[i])

for i in range(m + k):
    cmd,a,b = map(int,input().split())

    if cmd == 1:
        updateValue(a-1, b)
        #print()
        #displaySegmentTree()
    else:
        print(getSegmentSum(a-1,b-1))