from copy import deepcopy

def solution(board):
    n, m = len(board), len(board[0])
    answer = n * m
    bom_list = list()
    search = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                bom_list.append([i, j])
    
    answer -= len(bom_list)
    check_list = deepcopy(bom_list)           
    for bom in bom_list:
        for k in range(8):
            ki = bom[0] + search[k][0]
            kj = bom[1] + search[k][1]
            
            if 0 <= ki < n and 0 <= kj < m and [ki, kj] not in check_list:
                answer -= 1
                check_list.append([ki, kj])
        
        
    return answer