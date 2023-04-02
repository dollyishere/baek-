import sys
from collections import deque

N = int(sys.stdin.readline())

my_card = deque([i for i in range(1, N + 1)])

while len(my_card) != 1:
    my_card.popleft()
    if len(my_card) > 1:
        new_card = my_card.popleft()
        my_card.append(new_card)

print(my_card.pop())
