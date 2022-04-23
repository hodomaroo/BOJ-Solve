import sys
input = sys.stdin.readline

from math import log2,ceil

n,m = map(int,input().split())
depth = ceil(log2(n)) + 1
#데이터 - 순으로 해서 넣어주기 --?
#"""
def displaySegmentTree():
    index = 1
    dis = 1
    while index < len(segmentTreeNodes):
        sepa = segBaseNodes // dis - 1
        print(" " * sepa,end = "")
        print(*segmentTreeNodes[index: index + dis],sep=" " * (sepa * 2 + 1))
        index += dis
        dis *= 2
#"""

#최소 / 최대
segmentTreeNodes = [[float("inf"),-float("inf")] for _ in range(pow(2,depth))]
#print(segmentTreeNodes)
segBaseNodes = pow(2,depth-1)

#print(len(segmentTreeNodes),segBaseNodes)
def getNthNodes(index : int) -> int:
    return len(segmentTreeNodes) - segBaseNodes + index

def updateValue(targetNode : int, value : int): #갱신하면서 올라가기
    targetNode = getNthNodes(targetNode)
    segmentTreeNodes[targetNode] = [value,value]

    #print(targetNode,value)

    #짝수노드면 홀수노드가 Brother / 아니면 짝수노드가 Brother Node

    while targetNode:
        brotherNode = targetNode - (targetNode % 2) + (targetNode % 2 == 0)
        segmentTreeNodes[targetNode // 2] = [min(segmentTreeNodes[targetNode][0],segmentTreeNodes[brotherNode][0]),max(segmentTreeNodes[targetNode][1],segmentTreeNodes[brotherNode][1])]
        targetNode //= 2 #위로 올라가면서 부모값 갱신

def getSegmentSum(wantLeft : int, wantRight : int) -> int:
    return getAreaSum(1,0,segBaseNodes-1,wantLeft,wantRight)

def getAreaSum(node : int, start: int, end: int, wantLeft: int, wantRight: int) -> int:
    #원하는 영역의 합 구하기
    #print(node,start,end,wantLeft,wantRight)
    mid = (start + end) // 2
    if (start,end) == (wantLeft,wantRight): #영역이 동일하면 해당 세그먼트 값 리턴하기
        return segmentTreeNodes[node]

    minValue,maxValue = float("inf"),-float("inf")
    if wantLeft <= mid:
        v1, v2 = getAreaSum(node * 2, start, mid, wantLeft, min(wantRight, mid))
        minValue = min(v1,minValue)
        maxValue = max(v2,maxValue)

    if wantRight > mid:
        v1, v2 = getAreaSum(node * 2 + 1, mid + 1, end, max(mid + 1, wantLeft), wantRight)
        minValue = min(v1, minValue)
        maxValue = max(v2, maxValue)

    return (minValue,maxValue)


numberList = [int(input()) for _ in range(n)]
for i in range(len(numberList)):
    updateValue(i,numberList[i])
#displaySegmentTree()

for i in range(m):
    a,b = map(int,input().split())
    print(*getSegmentSum(a-1,b-1))

