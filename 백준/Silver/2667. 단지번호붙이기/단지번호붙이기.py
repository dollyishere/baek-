import sys
from collections import deque

# 지도 가로 세로 길이 N을 받아줌
N = int(sys.stdin.readline())

# 현재 지도 상황을 2차원 배열 리스트인 alcom에 받아줌
alcom = [[int(n) for n in sys.stdin.readline().strip()] for _ in range(N)]

# 각 집의 좌표를 담아줄 apart, 단지를 담아줄 comp 빈 리스트 각각 생성
apart = list()
comp = list()

# 2중 for문 이용해 alcom 각 좌표 조회하면서 만약 집이 존재할 경우(해당 좌표값 1일 시) apart에 해당 좌표를 리스트 형태로 저장
for i in range(N):
    for j in range(N):
        if alcom[i][j]:
            apart.append([i, j])

# 델타탐색용 리스트 di, dj 생성
di = [0, 1, -1, 0]
dj = [1, 0, 0, -1]

# 방문 기록용 리스트 visited 생성
visited = [[0] * N for _ in range(N)]

# bfs 수행
# apart의 각 좌표(집들) for문으로 순회함
# 만약 해당 좌표가 이미 방문한 좌표라면, 굳이 순회할 필요 없음(이미 다른 단지에 포함되어있다는 뜻임)
for a in apart:
    # 만약 아직 방문하지 않은 집이라면, 해당 좌표를 queue에 미리 넣어준 후, 해당 좌표를 방문한 것으로 처리함
    # 해당 단지에 몇 채의 집이 존재하는지를 체크할 cnt 변수 생성함
    if not visited[a[0]][a[1]]:
        queue = deque([a])
        visited[a[0]][a[1]] = 1
        cnt = 0
        # queue가 빌 때까지 반복
        # 먼저 cnt에 1을 더해준 후, 선입 선출 원칙 대로 queue deque에서 가장 앞에 위치한 값을 popleft로 빼서 변수 v에 저장
        # 파악을 쉽게하기 위해, 임의 변수 i, j에 v의 0인덱스, 1인덱스 값 각각 배정  
        while queue:
            cnt += 1
            v = queue.popleft()
            i, j = v[0], v[1]
            # 델타탐색 진행
            # 만약 해당 ni, nj가 지도의 범위 내에 있고, 좌표 값이 1이며, 아직 방문하지 않았을 시, queue에 추가해준 후 방문했다고 기록함
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N and alcom[ni][nj] and not visited[ni][nj]:
                    queue.append([ni, nj])
                    visited[ni][nj] = 1
        # bfs를 마친 후, cnt를 comp에 추가해줌
        comp.append(cnt)

# sort를 이용해 comp 내의 값을 오름차순으로 정렬해줌
comp.sort()

# 모든 연산 마친 후, comp 내에 존재하는 단지 수와 해당 단지의 값들을 차례대로 출력함
print(len(comp))
for c in comp:
    print(c)