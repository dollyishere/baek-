import heapq
import sys

h = []
n = int(sys.stdin.readline())
for _ in range(n):
    now_input = int(sys.stdin.readline())
    if now_input:
        heapq.heappush(h, -now_input)
    else:
        if h:
            print(-heapq.heappop(h))
        else:
            print(0)