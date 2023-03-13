# 재귀형 dfs인데 runtime 걸렸으므로...일단 기록

# 정점 수 N, 간선 수 M, 시작 정점 R 각각 입력
N, M, R = map(int, input().split())

# 각 정점 간 연결 상태 넣어줄 map_list, 방문 기록할 visited 각각 생성
# 이때 간선은 1부터 시작하므로, N+1을 기준으로 만들어줌
map_list = list([] for _ in range(N + 1))
visited = [0] * (N + 1)

# 이후 시작 정점 R 값을 dfs에 쓸 stack에 미리 넣어줌
# 방문 번호 기록할 dfs_cnt도 미리 생성(초기 값 1)
stack = [R]
dfs_cnt = 1

# dfs 함수 제작함
# visited, dfs_cnt를 global 선언한 후, 이후 아래에서 방문 기록할 수 있도록 함
def dfs(stack):
    global visited
    global dfs_cnt

    # stack에 값이 존재할 때, 즉, 아직 갈 수 있는 간선이 남아있을 때까지 while문으로 반복
    while stack:
      # 이번에 방문할 node의 번호를 stack을 통해 뒤에서 빼옴
      go_node  = stack.pop()
      # 만약 아직 방문하지 않을 node일 시, visited[go_node]의 값(초기값 0)을 dfs_cnt로 바꿔줌
      # 이후 dfs_cnt에 1 더해준 후, map_list에 기록된 갈 수 있는 node들을 stack에 extend하여 추가해줌
      if visited[go_node] == 0:
          visited[go_node] = dfs_cnt
          dfs_cnt += 1
          stack.extend(map_list[go_node])
    
# 입력된 간선 상황을 map_list에 기록함
# 간선 정보 u, v를 입력 받아 정수로 전환함
# 이후 양방향 연결 상태를 기록함
for m in range(M):
    u, v = map(int, input().split())
    map_list[u].append(v)
    map_list[v].append(u)

# 또한, 정점 번호를 오름차순으로 방문한다고 명시되어 있으므로, sort로 정리해줌
# 단, stack을 이용할 예정이므로 역순으로 정렬함(뒤에서부터 값을 빼오기 때문에)
for m in range(N + 1):
    map_list[m].sort(reverse=True)

# dfs 실행함
dfs(stack)

# # 이후 visited에 기록되어 있는 결과를 출력함
for visited_num in range(1, N + 1):
    print(visited[visited_num])