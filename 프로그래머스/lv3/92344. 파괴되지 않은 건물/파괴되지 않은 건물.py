def solution(board, skill):
    matrixPrefixSum = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
        
    for oper, r1, c1, r2, c2, degree in skill:
        dir = [-1, 1][oper - 1]
        matrixPrefixSum[r1][c1] += degree * dir
        matrixPrefixSum[r2 + 1][c2 + 1] += degree * dir
        matrixPrefixSum[r1][c2 + 1] -= degree * dir
        matrixPrefixSum[r2 + 1][c1] -= degree * dir
        
    
    for i in range(len(board)):
        for j in range(1,len(board[0])):
            matrixPrefixSum[i][j] += matrixPrefixSum[i][j - 1]
    
    for j in range(len(board[0])):
        for i in range(1, len(board)):
            matrixPrefixSum[i][j] += matrixPrefixSum[i - 1][j]
    
    #print(*matrixPrefixSum, sep = "\n")
    return sum(board[i][j] + matrixPrefixSum[i][j] > 0 for j in range(len(board[0])) for i in range(len(board)))
            
        
        
        
    
    
    return answer