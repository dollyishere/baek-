from collections import deque

# 모눈종이 크기 n, m을 입력 받음
# 이후 현재 치즈의 전체적인 상태 담아줄 cheeze_map 생성
# 그리고 n동안 현재 치즈 상태 입력받아 cheeze_map에 저장
n, m = map(int, input().split())
cheeze_map = []

for _ in range(n):
    cheeze_map.append(list(map(int, input().split())))

cheeze_state = deque()
moving = [[0, 1], [0, -1], [1, 0], [-1, 0]]
complete_melt_cnt = 0

for i in range(n):
    for j in range(m):
        if cheeze_map[i][j]:
            cheeze_state.append([i, j])

while cheeze_state:
    # 외부의 while문이 시작할 때마다 complete_melt_cnt에 1씩 증가하게 됨
    cheeze_state = deque()
    complete_melt_cnt += 1
    air_queue = deque()
    visited_list = [[0] * m for _ in range(n)]
    air_queue.append([0, 0])
    visited_list[0][0] = 1
    while air_queue:
        now_air_part = air_queue.popleft()
        for k in range(4):
            di = now_air_part[0] + moving[k][0]
            dj = now_air_part[1] + moving[k][1]
            if 0 <= di < n and 0 <= dj < m and visited_list[di][dj] == 0:
                if cheeze_map[di][dj] != 0:
                    cheeze_map[di][dj] += 1
                else:
                    visited_list[di][dj] = 1
                    air_queue.append([di, dj])
    
    for i in range(n):
        for j in range(m):
            if cheeze_map[i][j] >= 3:
                cheeze_map[i][j] = 0
            else:
                if cheeze_map[i][j] != 0:
                    cheeze_map[i][j] = 1
                    cheeze_state.append([i, j])

    
# 모든 치즈가 녹은 후, 정답인 complete_melt_cnt를 출력
print(complete_melt_cnt)



# 외부/내부 공기 검증 안해서 틀린거....
# 아까워서 그냥 놔둠(이런 문제 만들어줘~실버 3정도로)
# from collections import deque
# from pprint import pprint

# # 모눈종이 크기 n, m을 입력 받음
# # 이후 현재 치즈의 전체적인 상태 담아줄 air_state 생성
# # 그리고 n동안 현재 치즈 상태 입력받아 air_state에 저장
# n, m = map(int, input().split())
# air_state = []

# for _ in range(n):
#     air_state.append(list(map(int, input().split())))

# # 이제 치즈의 각 파트를 담아줄 cheeze_state, 녹아 없어질 치즈 담아줄 melt_cheeze_state를 deque()로 생성
# # deque를 사용하는 것은 bfs를 위함임
# # 이후 치즈가 공기에 몇 개의 면이나 접촉했는지 확인할 좌표 담을 moving 생성
# # 정답으로 출력할, 치즈가 모두 녹는 시간 담아줄 complete_melt_cnt 생성해줌
# cheeze_state = deque()
# melt_cheeze_state = deque()
# moving = [[0, 1], [0, -1], [1, 0], [-1, 0]]
# complete_melt_cnt = 0

# # 본격적으로 bfs 시작하기 앞서, air_state를 순회하면서 치즈가 놓인 좌표는 전부 cheeze_state에 담아줌
# for i in range(n):
#     for j in range(m):
#         if air_state[i][j]:
#             cheeze_state.append([i, j])

# # 이제 bfs 실행
# # 본 문제의 경우, 치즈가 모두 녹을 때를 시간 단위(1시간)로 검증해야함
# # 따라서 while문을 중복해서 사용하게 됨
# # 외부의 while문은 매 1시간의 반복임
# # 내부의 while문은 모든 치즈를 순회하며 녹을지 안녹을지의 여부를 판별하는 반복문(bfs)임
# while cheeze_state:
#     pprint(air_state)
#     # 따라서, 외부의 while문이 시작할 때마다 complete_melt_cnt에 1씩 증가하게 됨
#     complete_melt_cnt += 1
#     # now_cheeze_state라는 변수를 deque로 생성해준 다음, 현재 cheeze_state에 담겨 있는 치즈의 좌표를 extend로 넣어줌
#     # 그리고 다음 치즈 상태 검증을 위해 cheeze_state를 초기화해줌
#     now_cheeze_state = deque()
#     now_cheeze_state.extend(cheeze_state)
#     cheeze_state = deque()
#     # 이제 now_cheeze_state가 빌 때까지 검증함
#     while now_cheeze_state:
#         # 현재 검증하는 치즈의 좌표를 popleft로 빼내어 now_air_part에 담아줌
#         now_air_part = now_cheeze_state.popleft()
#         # 현재 치즈 블록이 몇 면이나 공기에 닿았는지 확인할 air_cnt 생성
#         air_cnt = 0
#         # 치즈의 사면에 붙어있는 블록에 대한 델타탐색 실시함
#         for k in range(4):
#             di = now_air_part[0] + moving[k][0]
#             dj = now_air_part[1] + moving[k][1]
#             # 만약 치즈와 이웃하는 블록이 범위에서 벗어나지 않았으며 현재 치즈가 존재하지 않을 시,
#             # 공기와 접촉했다는 뜻이므로 air_cnt에 1씩 추가함
#             if 0 <= di < n and 0 <= dj < m and air_state[di][dj] == 0:
#                 air_cnt += 1

#         # 만약 air_cnt가 2 미만일 시, 해당 치즈는 1시간 후에도 녹지 않는다는 뜻임
#         # 따라서 cheeze_state에 해당 좌표를 다시 넣어주어 다음 1시간 후에 다시 검증하게 함
#         if air_cnt < 2:
#             cheeze_state.append(now_air_part)
#         # 만약 치즈가 현 1시간 동안 녹을 운명이라면, melt_cheeze_state에 해당 좌표값을 저장해줌
#         # 바로 치즈를 녹음 처리하지 않는 이유는, 다른 치즈 블록을 검증할 때 영향을 받아서는 안되기 때문임(중요)
#         else:
#             melt_cheeze_state.append(now_air_part)

#     # 모든 연산이 끝나기 전, 다음 검증을 위해 녹을 운명인 치즈 블록 좌표 내부 값을 변경해주어야 함
#     # melt_cheeze_state가 빌 때까지 while문을 순회하며, 해당 좌표 내부 값을 0으로 변경해줌
#     while melt_cheeze_state:
#         melt_cheeze = melt_cheeze_state.popleft()
#         air_state[melt_cheeze[0]][melt_cheeze[1]] = 0
    
# # 모든 치즈가 녹은 후, 정답인 complete_melt_cnt를 출력
# print(complete_melt_cnt)
