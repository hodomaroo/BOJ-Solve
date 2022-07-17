from typing import List
from heapq import heappop,heappush

def solution(jobs : List[List[int]]) -> int:
    jobs.sort(key=lambda x : -x[0]) #정렬
    heap = []
    
    mod = len(jobs)
    time = 0
    totalWait = 0
    
    while jobs or heap:
        while jobs and (jobs[-1][0] <= time or not heap):
            heappush(heap,jobs.pop()[::-1]) 
        
        last, start = heappop(heap)
        
        if time < start:
            time = start
            
        time += last
        totalWait += time - start
        
    return totalWait // mod