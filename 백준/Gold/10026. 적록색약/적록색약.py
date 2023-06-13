import sys
from collections import deque

# 가로 세로 길이인 n과 queue 생성
n = int(sys.stdin.readline())
map_state = []
queue = deque()
# 방문 기록할 visited_list 생성
visited_list = [[0] * n for _ in range(n)]
# 델타탐색용 이동 좌표 생성
can_move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 적록색약이 아닌 경우(can_see), 색약인 경우(cant_see)를 각각 담아줄 리스트 생성
can_see = []
cant_see = []

# n만큼 현재 구역 상태 받아와줌
for _ in range(n):
    map_state.append(sys.stdin.readline().rstrip("\n"))

# bfs 실행
# 이때 현재 queue 상태, 현재 어떤 색인지(now_mine), 색약인지 아닌지(case)를 인자로 받음
def bfs(queue, now_mine, case):
    global visited_list
    # 그룹에 해당되는 수를 카운트할 group_block_cnt 생성
    group_block_cnt = 1
    # queue가 모두 빌 때까지 while문 실행
    while queue:
        now_here = queue.popleft()
        for k in range(4):
            di = now_here[0] + can_move[k][0]
            dj = now_here[1] + can_move[k][1]
            if 0 <= di < n and 0 <= dj < n and visited_list[di][dj] != 1:
                # 색약일 시, now_mine값이 R이나 G면 둘 다 동등하게 취급
                if case:
                    if now_mine == "R" or now_mine == "G":
                        if map_state[di][dj] == "R" or map_state[di][dj] == "G":
                            queue.append([di, dj])
                            group_block_cnt += 1
                            visited_list[di][dj] = 1
                    else:
                        if map_state[di][dj] == now_mine:
                            queue.append([di, dj])
                            group_block_cnt += 1
                            visited_list[di][dj] = 1
                # 색약이 아닐 시, 셋 다 별개로 취급
                else:
                    if map_state[di][dj] == now_mine:
                        queue.append([di, dj])
                        group_block_cnt += 1
                        visited_list[di][dj] = 1
    return group_block_cnt

# 색약이 아닌 경우, 색약일 경우 각각 분류하여 bfs 실행
# 이때 색약이 아닌 경우 검증을 마친 후, visited_list를 초기화해줌
for i in range(n):
    for j in range(n):
        if visited_list[i][j] != 1:
            queue.append([i, j])
            visited_list[i][j] = 1
            can_see.append(bfs(queue, map_state[i][j], False))

visited_list = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited_list[i][j] != 1:
            queue.append([i, j])
            visited_list[i][j] = 1            
            cant_see.append(bfs(queue, map_state[i][j], True))

print(len(can_see), len(cant_see))

