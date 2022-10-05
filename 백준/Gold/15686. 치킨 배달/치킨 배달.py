def total_i(arr):
    total = 0
    check = [[] for _ in range(M)]
    for a in range(M):
        v = chicken_house[arr[a]]
        for house in houses:
            val = abs(v[0] - house[0]) + abs(v[1] - house[1])
            check[a].append(val)
    for i in range(len(houses)):
        minv = float('INF')
        for j in range(M):
            if check[j][i] < minv:
                minv = check[j][i]
        total += minv
    return total

def dfs(i):
    global answer
    if len(stack) == M:
        if total_i(stack) < answer:
            answer = total_i(stack)
        return
    else:
        for j in range(i, len(chicken_house)):
            if j not in stack:
                stack.append(j)
                dfs(j)
                stack.pop()

N, M = map(int, input().split())
mapping = [list(map(int, input().split())) for _ in range(N)]

houses, chicken_house = list(), list()

for i in range(N):
    for j in range(N):
        if mapping[i][j] == 2:
            chicken_house.append([i, j])
        elif mapping[i][j] == 1:
            houses.append([i, j])

answer = float('INF')
stack = list()

dfs(0)

print(answer)