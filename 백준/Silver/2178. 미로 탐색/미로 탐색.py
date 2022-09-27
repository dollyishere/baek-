import sys
from collections import deque

# dfs는 시! 간! 초! 과!
# my 경각심을 위해...그리고 dfs 그럭저럭 짠 게 조금 뿌듯해서 걍 놔둠...

# v를 인자로 갖는 dfs 함수 f 선언
def f(v):
    # 정답인 최소값 담아줄 변수 minv를 글로벌 선언해줌
    global minv

    # v는 좌표값이므로, 각각 i, j라는 임의의 변수에 나눠담아줌
    i, j = v[0], v[1]
    # 만약 목표점([N-1, M-1])에 도달했다면, 현재까지 stack에 담긴 좌표 수를 구해본 후에 minv와 대조
    # 대조해본 후 현재 minv값보다 짧다면, 해당 값으로 minv 값을 교체해준 후, pop 진행해서 맨 뒷값(그러니까 목표지점 값) 빼줌
    # 만약에 목표지점 값 굳이 stack에 append 안해주고 pop도 진행 안하고 맨 마지막에 최종 minv값 출력할 때 1 더하는 것도 방법 중 하나임
    if v == [N - 1, M - 1]:
        # stack.append([N - 1, M - 1])
        if len(stack) < minv:
            minv = len(stack)
        # stack.pop()
        return
    # 만약 현재 stack의 길이가 minv 값보다 크거나 같다면, 가망이 없다는 뜻임. 그대로 return함
    elif len(stack) >= minv:
        return
    # 만약 위의 두 탈출 조건에 속하지 않는다면, 이하 연산을 진행함
    else:
        # 만약 stack 안에 해당 정점이 들어있지 않다면, stack에 v를 추가해준 후, 델타 탐색을 진행함
        # 만약 ni, nj 값이 미로 범위 내에 있으며, 해당 좌표가 이동할 수 있는 칸(값 1)이라면, 재귀 진행함
        # 재귀가 끝난 후, stack에서 현재 정점 값 제거해줌(나중에 다른 루트 탈 때 밟을 수 있도록) 
        if v not in stack:
            stack.append(v)
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M and miro[ni][nj]:
                    f([ni, nj])
            stack.pop()

# 미로의 세로 가로 길이 N, M 각각 정수 형태로 입력받아줌
N, M = map(int, sys.stdin.readline().split())
# 2중 for문을 통해 현 미로 상태를 받아와줌
miro = [[int(m) for m in sys.stdin.readline().strip()] for _ in range(N)]
# 정답 출력할 minv 변수에는 파이썬에서 가능한 최대값('INF')을 부여함
minv = 0

# 델타탐색용 리스트 di, dj 생성
di = [0, 1, -1, 0]
dj = [1, 0, 0, -1]

# 이후 bfs 수행할 때 사용할 빈 리스트 stack을 만들어줌
# 여기서는 stack을 queue용으로 쓸거임(이름이 왜 저러냐면 원래 dfs용으로 쓴거라...)
# deque선언해준 후 초기 값으로 시작점 좌표 [0, 0]를 삽입해줌
stack = deque([[0, 0]])

# 방문기록용 visited 생성
# 첫 정점 값(좌표 0, 0)을 이미 방문한 것으로 변경해줌
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1

# 총 몇 번 반복했는지를 기록할 변수 cnt를 지정
cnt = 0
# stack이 빌 때까지 while문으로 반복(정확한 횟수를 우리는 모른다)
while stack:
    # stack 새로 비우기 시작할 때마다 cnt에 1씩 더해줌
    cnt += 1
    # 현재 stack 내부의 요소들의 수만큼 for문으로 반복함
    # stack 내에 들어있는 정점들을 선입선출, popleft를 이용해 빼내줌
    # 임의 변수 i, j에 v의 각 가로 세로 좌표를 넣어줌
    # 만약에 v가 목표 지점이라면, 현재까지의 cnt를 출력해준 후 while문 탈출해줌
    for _ in range(len(stack)):
        v = stack.popleft()
        i, j = v[0], v[1]
        if v == [N - 1, M - 1]:
            print(cnt)
            break
    # 만약 목표지점이 아니라면, 갈 수 있는 곳 탐색해서 stack에 추가로 넣어줘야 함
    # 델타탐색 진행
    # 만약 해당 ni, nj 값이 미로 범위 내에 있고, 이동할 수 있으며(값이 1), 아직 방문하지 않은 인덱스라면,
    # 일단 stack에 해당 좌표를 길이 2인 리스트 형태로 넣어준 후, visited 해당 좌표 값을 1로 바꿔주는 것으로 방문 표기를 해줌
        else:
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M and miro[ni][nj] and not visited[ni][nj]:
                    stack.append([ni, nj])
                    visited[ni][nj] = 1
