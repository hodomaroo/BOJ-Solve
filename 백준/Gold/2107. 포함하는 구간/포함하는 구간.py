from heapq import heappop,heappush

n = int(input())
area = [list(map(int,input().split())) for _ in range(n)]

start = []
linear = []

for i in range(0,len(area)):
    start.append(area[i])
    linear.append(area[i])
    linear.append(area[i][::-1])
start.sort(reverse=True)
linear.sort(reverse=True)
ans = 0
areaHeap = []
closed = set()

#print(start,linear)

while start:
    a,b = start.pop()
    if a in closed: continue

    while areaHeap and areaHeap[0][0] < a:
        heappop(areaHeap)

    while linear:
        x,y = linear.pop()
        if (x,y) == (b,a): break

        if x > y: #닫는구간인 경우 #이전에 시작한 구간의 닫는 구간일 순 없음
            closed.add(y)
            heappush(areaHeap,(y,x))

    ans = max(ans,len(areaHeap))

print(ans)
