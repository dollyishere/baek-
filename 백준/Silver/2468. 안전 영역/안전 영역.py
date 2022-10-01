from collections import deque
import sys

N = int(sys.stdin.readline())
mapping = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 1

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

max_rain = 0
for x in range(N):
    max_rain = max(max(mapping[x]), max_rain)

queue = deque([])
for n in range(max_rain - 1, -1, -1):
    check = [[0] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if mapping[i][j] > n:
                if not check[i][j]:
                    check[i][j] = 1
                    cnt += 1
                    queue.append([i, j])
                    while queue:
                        v = queue.popleft()
                        for k in range(4):
                            ni, nj = v[0] + di[k], v[1] + dj[k]
                            if 0 <= ni < N and 0 <= nj < N and not check[ni][nj] and mapping[ni][nj] > n:
                                queue.append([ni, nj])
                                check[ni][nj] = 1
                
                if cnt > answer:
                    answer = cnt

print(answer)