import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    now_order = sys.stdin.readline().split()
    
    if now_order[0] == "push_front":
        queue.appendleft(now_order[1])
    elif now_order[0] == "push_back":
        queue.append(now_order[1])
    elif now_order[0] == "pop_front":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif now_order[0] == "pop_back":
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif now_order[0] == "size":
        print(len(queue))
    elif now_order[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif now_order[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)