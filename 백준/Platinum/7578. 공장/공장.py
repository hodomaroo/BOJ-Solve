
from math import log2, ceil
import sys

n = int(input())
SEGMENT_HEIGHT = ceil(log2(n)) + 1
SEGMENT_BASE = pow(2, SEGMENT_HEIGHT - 1)
segment_tree = [0] * pow(2, SEGMENT_HEIGHT)

sys.setrecursionlimit(30)


def insert(index: int):  # [l,r)
    node = len(segment_tree) - SEGMENT_BASE + index
    segment_tree[node] = 1

    while node:
        node //= 2
        segment_tree[node] = segment_tree[node * 2] + \
            segment_tree[node * 2 + 1]


def get(node: int, left: int, right: int, leftLimit: int, rightLimit: int) -> int:
    # print(left, right, leftLimit, rightLimit)
    if left == leftLimit and right == rightLimit:
        return segment_tree[node]

    mid = (leftLimit + rightLimit) // 2
    _sum = 0
    if left < mid:  # [left, mid)
        _sum += get(node * 2, left, min(mid, right), leftLimit, mid)
    if mid < right:  # [mid, right)
        _sum += get(node * 2 + 1, max(left, mid), right, mid, rightLimit)

    return _sum


machineA = list(map(int, input().split()))
machineB = dict({v: i for i, v in enumerate(list(map(int, input().split())))})

_sum = 0

for index, v in enumerate(machineA):
    _sum += get(1, machineB[v], SEGMENT_BASE, 0, SEGMENT_BASE)
    insert(machineB[v])

print(_sum)
