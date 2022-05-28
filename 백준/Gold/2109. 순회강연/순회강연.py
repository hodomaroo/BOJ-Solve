from heapq import heappop,heappush

n = int(input())
inform = sorted([list(map(int,input().split())) for _ in range(n)],key=lambda x : x[-1])
#앞에 들어갈 수 있는 개수 순서대로 정렬함
#앞에 x가 들어갈 수 있는 애들 중 유효한 애들이 들어갈 수 있음

heap = []
for cost,limit in inform:
    if len(heap) == limit:
        if heap[0] > cost:
            continue
        heappop(heap)

    heappush(heap,cost)

print(sum(heap))