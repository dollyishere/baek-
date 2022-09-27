from collections import deque

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

relation = []
for _ in range(m):
    relation.extend(list(map(int, input().split())))

route = [[] for _ in range(n+1)]

for i in range(0, m*2, 2):
    route[relation[i]].append(relation[i+1])
    route[relation[i+1]].append(relation[i])

queue = deque([p1])
visited = [0] * (n + 1)
cnt = 0
flag = False

while True:
    if flag:
        break
    elif not queue:
        print(-1)
        break
    else:
        cnt += 1
        for _ in range(len(queue)):
            v = queue.popleft()
            if v == p2:
                print(cnt - 1)
                flag = True
                break
            elif not visited[v]:
                queue.extend(route[v])
                visited[v] = 1