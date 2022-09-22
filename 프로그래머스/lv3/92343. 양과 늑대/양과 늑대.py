def solution(info, edges):
    visit = [[False] * (2 << 18) for _ in range(len(info))]
    graph = [[] for _ in range(len(info))]
    mmax = 0
    
    for par,chi in edges:
        graph[par].append(chi)
        graph[chi].append(par)
    
    def dfs(node : int, lamb : int, wolf : int, stat : int) -> int: #stat : 이미 방문한 지점들
        if visit[node][stat] or lamb <= wolf : return #유효하지 않은 상태! ->
        print(node, lamb, wolf, stat)
        nonlocal mmax
    
        visit[node][stat] = True
        
        mmax = max(mmax, lamb)
        
        for nextnode in graph[node]:            
            if info[nextnode]:
                dfs(nextnode, lamb, wolf + info[nextnode] - ((stat >> nextnode) & 1), stat | (1 << nextnode))
            else:
                dfs(nextnode, lamb + 1 - info[nextnode] - ((stat >> nextnode) & 1), wolf, stat | (1 << nextnode))
    dfs(0, 1, 0, 1) 
    return mmax
        