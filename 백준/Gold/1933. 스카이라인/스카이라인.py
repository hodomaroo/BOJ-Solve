from heapq import heappop,heappush
from collections import Counter

counter = Counter([0])
heap,nodes = [0],[]

for _ in range(int(input())):
    l,h,r = map(int,input().split())
    nodes.append((l, h))
    nodes.append((r, -h))

nodes.sort(key=lambda x : (x[0],-x[1]))

lastPos = 0
area = 0

for pos,height in nodes:
    if height > 0: #추가하기
        if heap and abs(heap[0]) < height:
            print(pos,height,end=" ")

        heappush(heap, -height)
        counter[height] += 1
    else:
        counter[-height] -= 1 #카운터 감소시키기

        if heap and not counter[-heap[0]]:
            while heap and not counter[-heap[0]]:
                heappop(heap)  # 없어진 값은 그냥 제거하기
            print(pos, -heap[0],end=" ")