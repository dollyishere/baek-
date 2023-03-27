import sys
from collections import deque

# 상자 가로 세로 길이 M, N, 상자 상태 box_state 입력받음
M, N = map(int, sys.stdin.readline().split())
box_state = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 델타 탐색에 사용할 moving 지정
moving = [[0, 1], [0, -1], [1, 0], [-1, 0]]


# queue에 쓸 complete_tomato 리스트와 답으로 출력할 now_cnt 지정
complete_tomato = deque([])
now_cnt = 0

# box_state 순회하면서 만약 익은 토마토(1)가 있다면, 아래 태스크 수행
# now_cnt(익은 순서 값, 이 시점에서는 0) 값을 좌표값과 함께 compelete_tomato에 추가함
for n in range(N):
    for m in range(M):
        if box_state[n][m] == 1:
            complete_tomato.append([n, m, now_cnt])

# bfs 진행함
while complete_tomato:
    # 선입선출로 앞부터 빼옴
    now_tomato = complete_tomato.popleft()
    # now_cnt 값을 now_tomato[2] 값(익은 순서)으로 바꿔줌
    now_cnt = now_tomato[2]
    # 상하좌우로 델타 탐색 진행함
    for k in range(4):
        # 새 좌표값 지정해줌
        # 만약 새로운 좌표 값이 상자의 범위에서 벗어나지 않고, 해당 좌표 값이 안익은 토마토(0)라면,
        # 해당 좌표의 값을 1로 바꿔준 후 complete_tomato에 해당 좌표와 익은 순서를 넣어줌
        di = now_tomato[0] + moving[k][0]
        dj = now_tomato[1] + moving[k][1]
        if 0 <= di < N and 0 <= dj < M and box_state[di][dj] == 0:
            box_state[di][dj] = 1
            complete_tomato.append([di, dj, now_cnt + 1])

# 모든 bfs가 끝난 후, 다시 box_state를 순회
# 만약 아직도 box_state에 0 값이 존재한다면, 안익은 토마토가 아직 존재하는 것임
# 따라서 now_cnt 값을 -1로 바꿔준 후 break로 빠져나와 줌
for n in range(N):
    if 0 in box_state[n]:
        now_cnt = -1
        break

# 정답 출력함
print(now_cnt)