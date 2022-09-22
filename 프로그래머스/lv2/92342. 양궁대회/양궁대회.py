def solution(n, info):
    maxDiff, maxRem, maxStat = -1,0, -1
    
    def napsackDFS(remain : int, diff : int, stat : int, depth : int):
        nonlocal maxDiff, maxStat, maxRem
    
        if depth == 10:
            #print(maxremain)
            maxDiff,maxRem,maxStat = max((maxDiff,maxRem,maxStat), (diff,remain, stat))
            return
        
        if remain > info[depth]:
            napsackDFS(remain - info[depth] - 1,diff + 10 - depth, stat | (1 << (depth)), depth + 1)
            
        napsackDFS(remain, (diff - (10 - depth)) if info[depth] else diff, stat , depth + 1)
    
    napsackDFS(n, 0, 0, 0)
    print(maxDiff)
    return [(info[i] + 1) * ((maxStat >> i) & 1) for i in range(10)] + [maxRem] if maxDiff > 0 else [-1]
        

