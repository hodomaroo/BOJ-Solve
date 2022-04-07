from typing import List
import sys
input = sys.stdin.readline

def convertListToInt(nums : List) -> int:
    res = 0
    for v in nums:
        res = res * 10 + v

    return res

while True:
    nums = list(map(int,input().split()))
    if len(nums) == 1: exit()

    numsWithoutZero = []
    zeroCnt = 0

    for v in nums[1:]:
        if not v: zeroCnt += 1
        else: numsWithoutZero.append(v)

    numsWithoutZero.sort(reverse=True)
    lists = [[] for _ in range(2)]

    convert = False
    while zeroCnt or numsWithoutZero:
        if lists[convert] and zeroCnt:
            lists[convert].append(0)
            zeroCnt -= 1
        else:
            lists[convert].append(numsWithoutZero.pop())
        convert = not convert
    print(convertListToInt(lists[convert]) + convertListToInt(lists[not convert]))
