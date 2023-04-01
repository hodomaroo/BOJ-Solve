from bisect import bisect_left

n = int(input())
nums = list(map(int, input().split()))
sortedList: list[int] = []

for v in nums:
    if not sortedList or sortedList[-1] < v:
        sortedList.append(v)
        continue

    sortedList[bisect_left(sortedList, v)] = v
print(len(sortedList))