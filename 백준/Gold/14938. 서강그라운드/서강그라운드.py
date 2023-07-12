n, m, r = map(int, input().split())
map_state = [[m+1] * n for _ in range(n)]
items_cnt = list(map(int, input().split()))

for _ in range(r):
    line_state = list(map(int, input().split()))
    map_state[line_state[0]-1][line_state[1]-1] = line_state[2]
    map_state[line_state[1]-1][line_state[0]-1] = line_state[2]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if map_state[i][j] > map_state[i][k] + map_state[k][j] and (map_state[i][k] + map_state[k][j]) <= m:
                   map_state[i][j] = map_state[i][k] + map_state[k][j]

max_item = 0
for i in range(n):
    now_spot_total = 0
    for j in range(n):
        if map_state[i][j] <= m or i == j:
            now_spot_total += items_cnt[j]

    if now_spot_total > max_item:
        max_item = now_spot_total

print(max_item)