T = int(input())
for t in range(T):
    m, n, k = map(int, input().split())
    answer = 0
    moving = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    map_state = [[0] * m for _ in range(n)]
    not_visited = [[True] * m for _ in range(n)]

    for _ in range(k):
        now_cabage = list(map(int, input().split()))
        map_state[now_cabage[1]][now_cabage[0]] = 1

    for i in range(n):
        for j in range(m):
            if map_state[i][j] and not_visited[i][j]:
                queue = [[i, j]]
                not_visited[i][j] = False
                answer += 1
                while queue:
                    now_move = queue.pop(0)
                    for k in range(4):
                        di = now_move[0] + moving[k][0]
                        dj = now_move[1] + moving[k][1]
                        if 0 <= di < n and 0 <= dj < m and not_visited[di][dj] and map_state[di][dj]:
                            queue.append([di, dj])
                            not_visited[di][dj] = False
    
    print(answer)

