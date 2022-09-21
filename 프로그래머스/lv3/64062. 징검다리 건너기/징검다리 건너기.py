def solution(stones, k):
    """
    stones = sorted([[stones[i],i] for i in range(len(stones))], reverse = True) #전체 노드 한칸씩 밀기
    linkedList = [[i - 1 , i + 1] for i in range(len(stones))] #doubly Linked List
    #node0 -> start
    #node-1 -> end
    n = len(stones)
    
    
    nowAns,nowVal = 0,0
    
    while stones:    
        nowVal = stones[-1][0]
        while stones and stones[-1][0] == nowVal:
            nowVal, node = stones.pop()
            
            left,right = linkedList[node] #왼쪽 / 오른쪽 노드들
            
            if left >= 0:
                linkedList[left][1] = right
                
            if right < n:
                linkedList[right][0] = left
                
            if right - left > k:
                return nowVal
    return nowVal
    """
    
    stones = stones
    
    left,right = 0, 1e9
    
    while left + 1 < right:
        mid = (left + right) // 2
        
        prefix = 0
        flg = True

        for points in stones:
            prefix = prefix + 1 if points < mid else 0
            if prefix >= k:
                flg = False
                break
                
        if flg:
            left = mid
        else:
            right = mid
            
    return left
                