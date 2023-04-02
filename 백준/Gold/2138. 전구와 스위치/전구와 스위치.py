n = int(input())
prev = list(map(int, list(input())))
goal = list(map(int, list(input())))

_ans = 100001
for i in range(2):
    curPrev, curGoal, count = prev[:], goal[:], i
    if i:
        curPrev[0], curPrev[1] = not curPrev[0], not curPrev[1]

    for j in range(1, n):
        if curPrev[j - 1] != curGoal[j - 1]:
            count += 1
            for k in range(j - 1, min(n, j + 2)):
                curPrev[k] = not curPrev[k]

    if curPrev[-1] == curGoal[-1]:
        _ans = min(_ans, count)

print(-1 if _ans == 100001 else _ans)
