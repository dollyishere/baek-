from collections import deque

N, M = map(int, input().split())
queue = deque([(N, 0)])
visited = [0] * 100001

while queue:
    num, cnt = queue.popleft()
    if num == M:
        print(cnt)
        break
    if 0 <= num - 1 <= 100000 and not visited[num-1]:
        queue.append((num - 1, cnt + 1))
        visited[num-1] = 1
    if 0 <= num + 1 <= 100000 and not visited[num + 1]:
        visited[num + 1] = 1
        queue.append((num + 1, cnt + 1))
    if 0 <= num * 2 <= 100000 and not visited[num * 2]:
        queue.append((num * 2, cnt + 1))
        visited[num * 2] = 1