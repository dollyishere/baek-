def solution(board):
    answer = -1
    moving = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    queue = []
    robot_here = [0, 0]
    x, y = len(board), len(board[0])
    not_visited = [[True] * y for _ in range(x)]

    for i in range(x):
        for j in range(y):
            if board[i][j] == "R":
                robot_here = [i, j]
                queue.append([[i, j], 0])
                not_visited[i][j] = False
                break
    
    while queue:
        now_here = queue.pop(0)
        for k in range(4):
            di, dj = now_here[0][0], now_here[0][1]
            while 0 <= di < x and 0 <= dj < y and board[di][dj] != "D":
                di += moving[k][0]
                dj += moving[k][1]
            di -= moving[k][0]
            dj -= moving[k][1]

            if board[di][dj] == 'G':
                # print(di, dj)
                answer = now_here[1] + 1
                queue = []
                break
            elif not_visited[di][dj]:
                not_visited[di][dj] = False
                queue.append([[di, dj], now_here[1]+1])
    
    return answer