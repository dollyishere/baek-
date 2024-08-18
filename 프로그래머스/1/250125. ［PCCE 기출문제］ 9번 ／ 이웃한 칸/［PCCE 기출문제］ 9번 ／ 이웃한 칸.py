from pprint import pprint

def solution(board, h, w):
    now_color = board[h][w]
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    answer = 0
    
    for d in range(4):
        di, dj = h + delta[d][0], w + delta[d][1]

        if 0 <= di < len(board) and 0 <= dj < len(board[0]):
            if board[di][dj] == now_color:
                answer += 1
    
    return answer