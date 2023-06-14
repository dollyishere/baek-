import sys
from collections import deque 

# bfs + 델타

# 토마토가 담겨있는 상자 상황 담아줄 box_state 빈 리스트로 생성
box_state = []
# 하나의 토마토가 인접할 수 있는 위치(위, 아래, 왼쪽, 오른쪽, 앞, 뒤) 좌표값 지정(h, n, m 순)
can_touch = [(0, 0, -1), (0, 0, 1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]
# 정답으로 출력할, 토마토가 모두 익는 데에 결리는 시간을 담아줄 days 변수 생성
days = 0
# 모두 익었는지 여부 확인할 all_ripe 변수 생성
all_ripe = True
# bfs 실행 시 필요한 queue 생성
queue = deque()


# 상자 가로 길이(m), 세로 길이(n), 그런 상자가 몇 개인지(h) 그 값을 입력받아 split로 따로 분류
m, n, h = map(int, sys.stdin.readline().split())

# 이제 상자 개수 만큼 for문으로 입력받아주기
for x in range(h):
    # 하나의 상자 상태만 담아줄 now_box 빈 리스트로 생성
    now_box = []
    # 상자 세로 길이만큼 for문 돌려 입력받은 값을 now_box에 저장
    # 이때 익은 토마토가 위치한 칸이라면, 해당 좌표값을 bfs를 위해 queue에 미리 저장해둠
    for y in range(n):
        now_line = list(map(int, sys.stdin.readline().split()))
        now_box.append(now_line)
        for z in range(m):
            if now_line[z] == 1:
                queue.append((x, y, z))
    # 현재 입력 받은 상자 상태 box_state에 저장
    box_state.append(now_box)

# 익힐 수 있는 토마토가 없을 때까지 반복함
while queue:
    # 날짜 별로 동시에 토마토를 익게 하기 위해 별도 queue 생성
    today_queue = deque()
    # 현재 queue에 저장되어 있는, 저번에 익은 토마토의 좌표 값을 today_queue에 extend로 저장한 후, queue는 다시 초기화 시킴
    today_queue.extend(queue)
    queue = deque()
    # today_queue가 빌 때까지 반복
    while today_queue:
        # 이번에 사용할 익힌 토마토 좌표값을 popleft()를 통해 빼온 후 ripe_tomato에 저장
        ripe_tomato = today_queue.popleft()
        # 해당 토마토로 6방향의 토마토를 익힐 수 있으므로, 6번 반복
        for k in range(6):
            # dx(현재 상자 층 수 + 인접한 토마토 좌표값), dy(현재 세로 위치 + 인접한 토마토 좌표값), dz(현재 가로 위치 + 인접한 토마토 좌표값) 각각 지정해줌
            dx = ripe_tomato[0] + can_touch[k][0]
            dy = ripe_tomato[1] + can_touch[k][1]
            dz = ripe_tomato[2] + can_touch[k][2]
            # 만약 dx, dy, dz 값이 범위에서 벗어나지 않고, 해당 좌표에 위치한 상자 칸에 안익힌 토마토가 들어 있다면,
            # queue에 해당 좌표값을 추가해준 후, box_state 값을 1로 전환시켜주면서 익혔다는 것을 표시
            if 0 <= dx < h and 0 <= dy < n and 0 <= dz < m and box_state[dx][dy][dz] == 0:
                queue.append((dx, dy, dz))
                box_state[dx][dy][dz] = 1
    # 이때 저장될 때부터 모든 토마토가 익어있는 상태인지도 검증해야 함
    # 만약 queue가 비어있다면, 이미 모든 토마토가 익어있는 상태이며, 추가로 토마토가 익을 수도 없음
    # 따라서 queue가 비어있지 않을 때만 days에 1을 추가해줌
    if queue:
        days += 1

# 이제 토마토가 모두 익었는지, 익지 못했는지를 검증
# 2 중 for문을 통해 모든 상자를 순회하면서 만약 0이 들어있을 경우, all_ripe 값을 False로 바꿔준 후 break로 빠져나옴
for x in range(h):
    for y in range(n):
        if 0 in box_state[x][y]:
            all_ripe = False
            break

# 만약 all_ripe 값이 True일 시, 며칠 걸렸는지(days)를 출력함
# False일 시, -1을 출력함
if all_ripe:
    print(days)
else:
    print(-1)
