import sys
from collections import deque

# 가로 n, 세로 m 길이, 맵 상태 map_state, 정답으로 출력할 find_map, 델타 탐색용 moving 각각 입력 받거나 만들어줌
n, m = map(int, sys.stdin.readline().split())
map_state = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
find_map = list(list(0 for _ in range(m)) for _ in range(n))
moving = [[0, 1], [0, -1], [1, 0], [-1, 0]]
break_time = False

# 2중 for문으로 map_state의 모든 인덱스 순회
# 만약 map_state[i][j]의 값이 2라면, 목표지점이라는 뜻임
# bfs(너비 우선 탐색을 진행, queue에는 [세로 위치, 가로 위치, 현재 카운트]를 넣어줌)한 후, 만약 while문을 탈출하면 for문에서도 탈출해줌
for i in range(n):
    if break_time:
        break
    for j in range(m):
        if map_state[i][j] == 2:
            queue = deque([[i, j, 0]])
            while queue:
                now_node = queue.popleft()
                for k in range(4):
                    di = now_node[0] + moving[k][0]
                    dj = now_node[1] + moving[k][1]
                    if 0 <= di < n and 0 <= dj < m and find_map[di][dj] == 0 and map_state[di][dj] != 2:
                        if map_state[di][dj] == 0:
                            find_map[di][dj] = 0
                        else:
                            find_map[di][dj] = now_node[2] + 1
                            queue.append([di, dj, now_node[2] + 1])
            break_time = True
            break

# 정해진 형식에 맞춰 정답 출력
# 다시 2중 for문 돌리면서 만약 갈 수 있는 공간인데도 못 도달하였다면 해당 인덱스 값을 -1로 바꿔줌
for i in range(n):
    for j in range(m):
        now_value = 0
        if map_state[i][j] == 1 and find_map[i][j] == 0:
            now_value = -1
        else:
            now_value = find_map[i][j]
        if j == m-1:
            print(now_value)
        else:
            print(now_value, end=' ')



                   
