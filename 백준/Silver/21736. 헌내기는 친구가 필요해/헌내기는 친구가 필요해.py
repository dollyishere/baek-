import sys
from collections import deque
# 델타탐색 + bfs

# 캠퍼스 상황 담아줄 map_state, 델타 탐색용 can_move, queue 용 리스트 각각 생성
map_state = []
can_move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
queue = deque()

# 맵 세로 가로 길이 각각 입력받아줌
n, m = map(int, sys.stdin.readline().split())

# 도연이가 만난 사람 수, 도연이가 방문한 캠퍼스 위치 확인할 i_meet, i_visited 각각 생성
i_meet = 0
i_visited = [[0] * m for _ in range(n)]

# 다음 n번만큼 캠퍼스 상황 입력받아 map_state에 저장
# 이때 readline 특성 상 뒤에 \n이 붙게 되므로 strip으로 제거해줌
for x in range(n):
    now_line = sys.stdin.readline().strip("\n")
    map_state.append(now_line)

    # 현재 도연이 위치 찾기
    # 만약 도연이의 위치를 찾으면 queue에 담아준 후, i_visited의 해당 좌표 내 값 변경
    for y in range(m):
        if now_line[y] == "I":
            queue.append([x, y])
            i_visited[x][y] = 1

# bfs 진행
# 델타 탐색 진행하면서, 만약 벽(X)이 아니고, 이미 방문하지 않은 구역일 시에만 검증함
# 만약 새로운 사람(P)을 만났을 시 i_meet에 1씩 추가
# 이후 방문한 구역 좌표는 다시 queue, i_visited에 좌표값(또는 1로 변경) 넣어준 후 queue가 다 빌때까지 while문으로 순회
while queue:
    now_here = queue.popleft()
    for k in range(4):
        di = now_here[0] + can_move[k][0]
        dj = now_here[1] + can_move[k][1]
        if 0 <= di < n and 0 <= dj < m and map_state[di][dj] != "X" and i_visited[di][dj] != 1:
            if map_state[di][dj] == "P":
                i_meet += 1
            queue.append([di, dj])
            i_visited[di][dj] = 1

# 델타탐색 완료 후, i_meet이 0일 시 TT 출력, 그렇지 않을 시 만난 사람 수 출력           
if i_meet:
    print(i_meet)
else:
    print('TT')
