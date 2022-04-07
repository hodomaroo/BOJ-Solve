import sys
input = sys.stdin.readline

while True:
    n,*nums = list(input().split())
    if len(nums) == 0: break

    numsWithoutZero = []
    zeroCnt = 0

    for v in nums:
        if v == "0": zeroCnt += 1
        else: numsWithoutZero.append(v)

    numsWithoutZero.sort(reverse=True)
    #print(numsWithoutZero)
    lists = [[] for _ in range(2)]

    convert = False
    while zeroCnt or numsWithoutZero:
        if lists[convert] and zeroCnt:
            lists[convert].append("0")
            zeroCnt -= 1
        else:
            lists[convert].append(numsWithoutZero.pop())
        convert = not convert

    #print(lists)
    print(int("".join(lists[convert])) + int("".join(lists[not convert])))
