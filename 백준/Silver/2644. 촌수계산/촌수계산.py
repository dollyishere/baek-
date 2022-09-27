from collections import deque

# 총 사람 수 n, 촌수 구하고 싶은 사람 p1, p2, 관계도 수 m을 각각 입력받음
n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

# 관계도 상태를 담아줄 빈 리스트 relation을 만들어줌
# for문 사용해 관계도 매줄 리스트 형태로 입력 받을 때마다 extend 하여 각 요소들을 그대로 relation에 append해줌
relation = []
for _ in range(m):
    relation.extend(list(map(int, input().split())))

# 파이썬은 초기 인덱스 값이 0이므로 사람 수 n보다 한칸 더 크게 하여 빈 리스트가 n+1만큼 든 2차원 리스트 route 생성
route = [[] for _ in range(n+1)]

# for문을 이용해 관계문을 인덱스 2씩 띄워 돌며 각 연결 상태를 route에 기록해줌
for i in range(0, m*2, 2):
    route[relation[i]].append(relation[i+1])
    route[relation[i+1]].append(relation[i])

# 구하고 싶은 중 한명의 값을 넣은 큐와 방문 기록 남겨줄 visited 리스트, 촌수 기록해줄 cnt와 이후 출력 여건 조절을 위한 flag 변수 생성
queue = deque([p1])
visited = [0] * (n + 1)
cnt = 0
flag = False

# bfs 진행, while True일때만 반복
# 만약 flag가 True로 바뀐다면, 그 즉시 while문 탈출함
while True:
    if flag:
        break
    # 만약 queue가 비어있다면, 촌수를 구할 수 없다는 뜻이므로 -1 출력한 후 while문 탈출함
    elif not queue:
        print(-1)
        break
    # 만약 위 조건에 모두 해당되지 않는다면, 이대로 진행함
    # cnt에 1 더해주고, 현재 queue에 담긴 각 값들 순회함
    # 선입선출 원칙을 지켜 queue의 맨 앞 값부터 먼저 꺼내어 변수 v에 저장해줌
    else:
        cnt += 1
        for _ in range(len(queue)):
            v = queue.popleft()
            # 만약 v의 값이 p2와 같다면, cnt에 -1한 후 출력
            # 그냥 cnt 값 출력할거면 초기 p1 값 기준으로 방문 기록한다던가 여러가지...조작을 해줘야 하기 때문에 그냥 이게 가장 맘 편함
            # 출력한 후에는 flag 값을 False에서 True로 바꿔준 후 for문 즉시 탈출
            if v == p2:
                print(cnt - 1)
                flag = True
                break
            # 만약 visited[v]의 현재 값이 0이라면, queue에 route[v]에 담긴 값을 extend로 해체하여 넣어준 후, 방문을 기록함
            elif not visited[v]:
                queue.extend(route[v])
                visited[v] = 1



