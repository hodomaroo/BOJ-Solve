from collections import defaultdict

n = int(input())
vals = list(map(int, input().split()))

valDict = defaultdict(set)
for i in range(n):
    valDict[vals[i]].add(i)

_ans = 0
for i in range(n):
    for j in range(i + 1, n):
        _sum = vals[i] + vals[j]

        other = valDict[_sum] - {i, j}
        _ans += len(other)

        remain = set()
        if i in valDict[_sum]:
            remain.add(i)
        if j in valDict[_sum]:
            remain.add(j)

        valDict[_sum] = remain
print(_ans)
