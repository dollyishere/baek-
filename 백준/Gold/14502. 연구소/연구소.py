from collections import deque

n, m = map(int, input().split())

lab_state = []

answer = 0
moving = [[0, 1], [1, 0], [-1, 0], [0, -1]]

for _ in range(n):
    now_line = list(map(int, input().split()))
    lab_state.append(now_line)

# dfs
def set_wall(wall_cnt):
    global lab_state
    if wall_cnt == 3:
        spread_virus()
        return
    for i in range(n):
        for j in range(m):
            if lab_state[i][j] == 0:
                lab_state[i][j] = 1
                set_wall(wall_cnt+1)
                lab_state[i][j] = 0

# bfs
def spread_virus():
    virtual_lab = [[0] * m for _ in range(n)]
    virus_list = deque()
    for i in range(n):
        for j in range(m):
            virtual_lab[i][j] = lab_state[i][j]
            if lab_state[i][j] == 2:
                virus_list.append([i, j])

    while virus_list:
        now_virus = virus_list.popleft()
        for k in range(4):
            di = now_virus[0] + moving[k][0]
            dj = now_virus[1] + moving[k][1]
            if 0 <= di < n and 0 <= dj < m:
                if virtual_lab[di][dj] == 0:
                    virtual_lab[di][dj] = 2
                    virus_list.append([di, dj])

    check_safe_area(virtual_lab)

def check_safe_area(virus_state):
    global answer
    safe_cnt = 0
    for i in range(n):
        for j in range(m):
            if virus_state[i][j] == 0:
                safe_cnt += 1
    answer = max(answer, safe_cnt)

set_wall(0)

print(answer)