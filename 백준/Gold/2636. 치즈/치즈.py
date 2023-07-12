from collections import deque

# 모눈종이 크기 n, m을 입력 받음
# 이후 현재 치즈의 전체적인 상태 담아줄 cheeze_map 생성
# 그리고 n동안 현재 치즈 상태 입력받아 cheeze_map에 저장
n, m = map(int, input().split())
cheeze_map = []

for _ in range(n):
    cheeze_map.append(list(map(int, input().split())))

cheeze_state = deque()
melt_cheeze_cnt = 0
moving = [[0, 1], [0, -1], [1, 0], [-1, 0]]
complete_melt_cnt = 0

for i in range(n):
    for j in range(m):
        if cheeze_map[i][j]:
            cheeze_state.append([i, j])

while cheeze_state:
    # 외부의 while문이 시작할 때마다 complete_melt_cnt에 1씩 증가하게 됨
    cheeze_state = deque()
    melt_cheeze_cnt = 0

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
            if cheeze_map[i][j] >= 2:
                cheeze_map[i][j] = 0
                melt_cheeze_cnt += 1
            elif cheeze_map[i][j] == 1:
                cheeze_state.append([i, j])

    
print(complete_melt_cnt)
print(melt_cheeze_cnt)
