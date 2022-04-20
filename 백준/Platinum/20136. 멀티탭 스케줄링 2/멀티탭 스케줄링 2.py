from collections import defaultdict,deque
from heapq import heappop,heappush

n,m = map(int,input().split())
multiUse = set()
schedule = list(map(int,input().split()))

valuePos = defaultdict(deque)

for i in range(len(schedule)):
    valuePos[schedule[i]].append(i)

count = 0
removeHeap = []

for i,value in enumerate(schedule):
    valuePos[value].popleft() #해당 값 스택에서 제거
    #print(value, multiUse,removeHeap)
    if value in multiUse or len(multiUse) < n:
        if value not in multiUse:
            multiUse.add(value)
        heappush(removeHeap,(-valuePos[value][0] if valuePos[value] else -float("inf"), value))
        continue

    while removeHeap:
        pos,val = heappop(removeHeap)
        if val == value or val not in multiUse or abs(pos) < i: continue #이전의 가비지값 or
        break

    multiUse.remove(val)
    heappush(removeHeap, (-valuePos[value][0] if valuePos[value] else -float("inf"), value))
    multiUse.add(value)
    count += 1

print(count)
