import sys
input = sys.stdin.readline

from math import log2,ceil

n,m,k = map(int,input().split())
depth = int(ceil(log2(n)))
segbaseNodes = pow(2,depth)
segmentTree = [[0,0] for _ in range(pow(2, depth + 1))] #segmentValue / lazyValue

def setLazySegmentValue(node: int, lower: int, upper: int, left: int, right: int, value: int) -> None:
    #print("S", left, right, lower, upper)
    if left == lower and right == upper:
        segmentTree[node][1] += value
    else:
        segmentTree[node][0] += (right - left) * value

    segmentTree[node][0] += (upper - lower) * segmentTree[node][1]

    if segmentTree[node][1] and node * 2 < len(segmentTree):
        segmentTree[node * 2][1] += segmentTree[node][1]
        segmentTree[node * 2 + 1][1] += segmentTree[node][1]

    segmentTree[node][1] = 0

    mid = (lower + upper) // 2

    if not (left == lower and right == upper):
        if left < mid: #[ )
            setLazySegmentValue(node * 2, lower, mid, left, min(mid, right), value)

        if right > mid: #오른쪽구간
            setLazySegmentValue(node * 2 + 1, mid, upper, max(mid, left), right, value)

def getLazySegmentValue(node: int, lower: int, upper: int, left: int, right: int) -> int:
    #print(left,right, lower,upper)
    segmentTree[node][0] += (upper - lower) * segmentTree[node][1] #내 구간 크기만큼 더해져야지 ㅋㅋㅋ

    if segmentTree[node][1] and node * 2 < len(segmentTree):
        segmentTree[node * 2][1] += segmentTree[node][1]
        segmentTree[node * 2 + 1][1] += segmentTree[node][1]

    segmentTree[node][1] = 0

    if left == lower and right == upper:
        return segmentTree[node][0]

    else:
        value = 0
        mid = (lower + upper) // 2

        if left < mid:  # [ )
            value += getLazySegmentValue(node * 2, lower, mid, left, min(mid, right))

        if right > mid:  # 오른쪽구간
            value += getLazySegmentValue(node * 2 + 1, mid, upper, max(mid, left), right)

        return value

for i in range(n):
    setLazySegmentValue(1, 0, segbaseNodes, i, i + 1, int(input()))

for i in range(m + k):
    query = input().split()

    if query[0] == "1":
        setLazySegmentValue(1,0, segbaseNodes, int(query[1]) - 1, int(query[2]), int(query[-1]))
    else:
        print(getLazySegmentValue(1, 0, segbaseNodes, int(query[1]) - 1, int(query[2])))






