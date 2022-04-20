from collections import defaultdict,deque

n,m = map(int,input().split())
multiUse = set()
schedule = list(map(int,input().split()))

valuePos = defaultdict(deque)

for i in range(len(schedule)):
    valuePos[schedule[i]].append(i)

count = 0
for i,value in enumerate(schedule):
    valuePos[value].popleft() #해당 값 스택에서 제거

    if value in multiUse:
        continue
    elif len(multiUse) < n:
        multiUse.add(value)
        continue

    maxVal,maxDist = 0,0

    for v in multiUse:
        dist = (valuePos[v][0] - i) if valuePos[v] else float("inf")
        if maxDist < dist:
            maxDist = dist
            maxVal = v

    multiUse.remove(maxVal)
    multiUse.add(value)
    count += 1
#print(multiUse)
print(count)
