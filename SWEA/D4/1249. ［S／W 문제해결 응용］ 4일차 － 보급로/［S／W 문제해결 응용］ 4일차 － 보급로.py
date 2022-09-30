# dp? 다익스트라?
from collections import deque

# 델타 탐색~~~~
di = [1, 0, 0, -1]
dj = [0, 1, -1, 0]

# 테스트 케이스 수 받아준 후 반복
T = int(input())

for tc in range(1, T+1):
    # 지도 가로 세로 길이 N 입력받기
    N = int(input())
    # 현재 지도 상태 각 변수 입력받아서 정수화한 후 리스트에 넣는 작업을 N만큼 반복(본 문제에서는 입력이 공백 안두고 붙여나옴)
    battlefield = [[int(i) for i in input()] for _ in range(N)]
    
    # BFS 사용
    # deque를 이용해 queue를 만들어준 후, 안에 튜플 형태의 시작점 좌표(0, 0), S와 걸리는 시간 저장용 cnt(초기값 0)을 넣어줌
    queue = deque([([0, 0], 0)])
    # 각 루트마다 시간 얼마나 걸리는지 최소값 기록한 후 비교해줄(dp처럼?) visited리스트를 만들어줌
    # 각 인덱스는 초기값을 무한대로 잡아준 후, 시작점 [0, 0]의 값만 0으로 변경함
    visited = [[float('INF')] * N for _ in range(N)]
    visited[0][0] = 0

    # bfs를 실행
    # 좌표와 현재까지 걸린 시간 popleft로 빼온 후 각각 v, cnt에 저장
    # i와 j에 v 내의 좌표값 쪼개서 저장함
    while queue:
        v, cnt = queue.popleft()
        i, j = v[0], v[1]
        # 델타탐색 진행, 기존에 만들어뒀던 델타탐색용 리스트 이용해서 ni, nj(해당 방향으로 이동했을 시 좌표값) 지정
        # 만약 해당 ni, nj값이 범위 내에 있다면, 이하 검증을 진행
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                # 현재 시간 값에 만약 해당 칸으로 이동했을 시 걸리는 시간을 계산해줌
                # 해당 값이 현재 해당 visited 좌표 값에 기록된 값보다 작다면, 해당 값으로 대체해준 후, 해당 루트 값을 기록해 queue에 저장함
                # 이로서 가장 최적의 이동 값만 queue에 저장되고, 앞으로도 계산될 것임(안하면 무한루프란다~)
                if visited[ni][nj] > cnt + battlefield[ni][nj]:
                    visited[ni][nj] = cnt + battlefield[ni][nj]
                    queue.append(([ni, nj], cnt + battlefield[ni][nj]))

    # 모든 연산을 마친 후, 해당 테스트 케이스 번호와 visited의 도착지점 G에 저장된 최소값 출력
    print('#{} {}'.format(tc, visited[N - 1][N - 1]))