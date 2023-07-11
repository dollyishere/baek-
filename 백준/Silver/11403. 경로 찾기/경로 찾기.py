import sys, math

# 정점 개수 n 입력받고, 그래프의 인접 행렬 상황 담아줄 graph_state 생성
# 이후 for문으로 그래프 인접 행렬 입력받음
n = int(input())
graph_state = []

for _ in range(n):
    graph_state.append(list(map(int, sys.stdin.readline().split())))

# 2중 for문으로 현재 인접 상황 확인함
# 만약 간선이 존재하지 않는다면(0) 구분하기 위해 inf로 값을 대체해줌
for i in range(n):
    for j in range(n):
        if graph_state[i][j] == 0:
            graph_state[i][j] = math.inf

# 3중 for문으로 플로이드-워셜 수행
# 여기서 현재 출발 정점은 j이고, 도착 정점은 k, 지나가는 중간 정점은 i라고 할 수 있음
# 만약 중간 정점을 지나쳐가는데 드는 거리가((graph_state[j][i] + graph_state[i][k])) j에서 k로 직접 향하는 거리(graph_state[j][k])보다 크다면,
# 중간 정점을 지나쳐가는 게 더 이득이므로, graph_state[j][k]의 값을 해당 값으로 바꿔줌
# 이를 반복하면서, 계속 더 빠른 거리로 전환시켜줌(dp랑 비슷한 듯?)
for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph_state[j][k] > (graph_state[j][i] + graph_state[i][k]):
                graph_state[j][k] = graph_state[j][i] + graph_state[i][k]

# 2중 for문을 통해 정답 출력
# 만약 값이 그대로 inf라면, 해당 정점에서 목표 정점까지 가는 경로가 없다는 것이므로(잘못 이해했을지도) 0을 출력
# 그 외에는 1을 출력(경로가 있으므로)
for i in range(n):
    for j in range(n):
        if j == n - 1:
            if graph_state[i][j] != math.inf:
                print(1)
            else:
                print(0)
        else:
            if graph_state[i][j] != math.inf:
                print(1, end=' ')
            else:
                print(0, end=' ')
