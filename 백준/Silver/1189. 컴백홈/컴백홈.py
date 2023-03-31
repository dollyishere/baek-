import sys

# 백트래킹용 함수 제작
def backtrack(here_list, now_index):
    # 출력할 결과 변수 answer을 global 선언함
    global answer

    # 만약 here_list의 길이가 K, 즉 갈 수 있는 거리를 모두 갔다면,
    # 현재 위치가 집([0, C-1])인지 확인하고 만약 맞다면 answer에 1 추가함
    if len(here_list) == K:
        if now_index == [0, C-1]:
            answer += 1

    # 만약 모든 거리를 다 가지 않았다면, 이후 절차 시행
    else:
        # 델타탐색 진행함
        for k in range(4):
            di = now_index[0] + moving[k][0]
            dj = now_index[1] + moving[k][1]
            # 만약 앞으로 탐색할 위치가 맵의 범위에서 벗어나지 않고,
            # 가지 못하는 곳도 아니고(T), 아직 방문하지도 않았다면,
            # here_list에 앞으로 탐색할 인덱스 추가해준 후 다시 백트래킹 돌림
            # 이후 더 많은 가능성의 탐색을 위해 here_list에서 pop으로 직전에 넣어둔 인덱스 제거해줌
            if 0 <= di < R and 0 <= dj < C:
              if map_state[di][dj] != 'T' and [di, dj] not in here_list:
                  here_list.append([di, dj])
                  backtrack(here_list, [di, dj])
                  here_list.pop()

# 맵의 세로 길이 R, 가로 길이 C, 가야하는 거리 K 각각 입력받음             
R, C, K = map(int, sys.stdin.readline().split())
# 맵 정보 담아줄 map_state 생성한 후 2중 for문으로 각 요소 다 분해해서 알맞게 넣어줌
map_state = []
for r in range(R):
    now_line = sys.stdin.readline()
    now_list = []
    for c in range(C):
        now_list.append(now_line[c])
    map_state.append(now_list)

# 델타탐색용 인덱스 값 넣어둔 moving 제작
moving = [[1, 0], [-1, 0], [0, 1], [0, -1]]
# 정답 카운팅 용으로 사용할 answer 제작
answer = 0

# 최초 출발지는 왼쪽 맨 아래임
# 맞는 인덱스 값을 넣어주고 백트래킹 시작
backtrack([[R - 1, 0]], [R - 1, 0])

# 모든 연산을 마친 후, 결과 출력
print(answer)